from prompts import *
import time
from openai import OpenAI
import os

def get_llm_response(prompt: str) -> str:
    api_key = os.getenv("OPENROUTER_API_KEY")
    if not api_key:
        raise ValueError("OPENROUTER_API_KEY environment variable not set")

    client = OpenAI(
        base_url="https://openrouter.ai/api/v1",
        api_key=api_key,
        default_headers={
            "HTTP-Referer": "https://github.com/your-project",  # Replace with your project
            "X-Title": "Your Application Name"  # Replace with your app name
        }
    )

    response = client.chat.completions.create(
        model="google/gemini-flash-1.5",
        messages=[{"role": "user", "content": prompt}]
    )

    return response.choices[0].message.content

def generate_augmentation(prompt, get_feedback_func,
                          max_retries, initial_delay, backoff_factor,
                          core_prompt=core_prompt,
                          toward_away_prompt=toward_away,
                          external_internal_prompt=external_internal,
                          options_procedures_prompt=options_procedures,
                          general_specific_prompt=general_specific,
                          representation_system_prompt=primary_representation):

    queries = {
        'toward_away': toward_away_prompt,
        'external_internal': external_internal_prompt,
        'options_procedures': options_procedures_prompt,
        'general_specific': general_specific_prompt,
        'representation_system': representation_system_prompt
    }

    responses = {}
    for key, query in queries.items():
        modified_query = query.replace("[Insert text to be analyzed here]", prompt)

        delay = initial_delay
        for attempt in range(max_retries + 1):
            try:
                responses[key] = get_feedback_func(modified_query)
                break
            except TimeoutError as timeout_exception:
                if attempt < max_retries:
                    print(f"Attempt {attempt + 1} for '{key}' failed. Retrying in {delay} seconds...")
                    time.sleep(delay)
                    delay *= backoff_factor
                else:
                    raise timeout_exception

    context_string = (
        f"The user's motivation style is likely: {responses['toward_away']}. "
        f"Their reference style is likely: {responses['external_internal']}. "
        f"They prefer: {responses['options_procedures']} over the other. "
        f"They prefer: {responses['general_specific']} information over the alternative. "
        f"Their primary representational system is likely: {responses['representation_system']}."
    )

    context_string = core_prompt.replace("[communication style preferences here]", context_string)
    return context_string

class ConversationManager:
    def __init__(self, get_response_func, get_feedback_func, n=5,
                 max_retries = 999, initial_delay=0.5, backoff_factor=2):

        self.conversation_history = []  # Stores the full conversation history
        self.base = None  # Stores the augmented base context
        self.exchange_count = 0  # Tracks the number of exchanges
        self.n = n  # The interval for regenerating the base context
        self.get_response_func = get_response_func
        self.get_feedback_func = get_feedback_func
        self.max_retries = max_retries
        self.initial_delay = initial_delay
        self.backoff_factor = backoff_factor

    def query(self, prompt, max_retries, initial_delay, backoff_factor):
        self.conversation_history.append(f"User: {prompt}")

        if self.exchange_count % self.n == 0:
            if self.base is None:
                self.base = generate_augmentation(prompt, self.get_feedback_func, max_retries, initial_delay, backoff_factor)
            else:
                history_for_augmentation = self.conversation_history[-2 * self.n:]
                self.base = generate_augmentation("\n".join(history_for_augmentation), self.get_feedback_func, max_retries, initial_delay, backoff_factor)

        augmented_prompt = self.base.replace("[User's original prompt here]", "\n".join(self.conversation_history))

        for attempt in range(max_retries + 1):
            try:
                response = self.get_response_func(augmented_prompt)
                break
            except TimeoutError as timeout_exception:
                if attempt < max_retries:
                    delay = initial_delay * (backoff_factor ** attempt)
                    print(f"Attempt {attempt + 1} failed. Retrying in {delay} seconds...")
                    time.sleep(delay)
                else:
                    raise timeout_exception

        self.conversation_history.append(f"Assistant: {response}")
        self.exchange_count += 1
        return response

    def set_n(self, n):
        """
        Update the value of n.

        Args:
            n (int): The new interval at which the base context is regenerated.
        """
        self.n = n

    def reset(self):
        """
        Resets the conversation history, base context, and exchange count.
        """
        self.conversation_history = []
        self.base = None
        self.exchange_count = 0

    def get_conversation_history(self):
        """
        Returns the full conversation history.

        Returns:
            list: The conversation history as a list of strings.
        """
        return self.conversation_history
