# MetaFlow: Attempt at Using LLMs for Personal Growth in Everyday Context  

**Enhance LLM interactions with unconscious preference detection and adaptive communication strategies**  

## Straight to The Point
Before I let R1 summarize everything in corporate-speak, here's the human perspective. 

For now, January 2025, reasoning models have their quirks. o1 is stubborn and refuses to admit technical mistakes. Claude Sonnet (not CoT, I know) is too agreeable and ready to change its mind at a moment's notice.

This library tries to find a "middle ground" by going deeper into what makes a conversation useful. It will prompt your LLMs to identify your unconscious preferences... and gently try and expand your comfort zone in each of those dimensions. I have a medium blog post in the writing to explain that further - I will replace this with a proper link when that's done.

In the meantime, enjoy the readme, courtesy of DeepSeek R1.

## Overview  
Tired of LLM chatbots that are either annoyingly agreeable - or stupidly stubborn?

MetaFlow aims to intelligently and subtly push users out of their comfort zone IF, and only IF it determines it is beneficial to their goals.

MetaFlow is a Python library that augments LLM prompts with insights about users' unconscious communication preferences derived from NLP meta-programs. By analyzing interaction patterns and strategically adapting responses, it:  
- 🧠 Detects cognitive preferences through 5 key meta-program dimensions  
- 🤖 Automatically tailors LLM communication style  
- ⚖️ Balances user comfort with cognitive growth   
- 🔄 Dynamically adapts through conversation context  

## Features  
- **NLP Meta-Program Analysis**: Profiles users across 5 cognitive dimensions  
- **Contextual Augmentation**: Enhances prompts with real-time style preferences  
- **Adaptive Strategies**: Maintains 80% preference alignment while introducing 20% cognitive stretch  
- **Conversation Management**: Maintains context-aware dialogue history with configurable refresh intervals  
- **Bias Mitigation**: Counteracts over-accommodation through strategic style variation  

## Installation  
```bash  
pip install metaflow  
```

## Usage

```python
from metaflow import ConversationManager  
from your_llm_provider import get_response, get_feedback  # Replace with actual LLM functions, according to your provider's API documentation 

# Initialize conversation manager  
manager = ConversationManager(
    get_response_func=get_response,
    get_feedback_func=get_feedback,
    n=3  # Refresh context every 3 exchanges
)

# First user message
user_prompt1 = "I need help organizing my work schedule"
response1 = manager.augmented_query(user_prompt1)
print(f"Assistant: {response1}")

# Follow-up exchange
user_prompt2 = "I keep getting distracted by emails"
response2 = manager.augmented_query(user_prompt2)
print(f"\nAssistant: {response2}")

# Deeper exploration
user_prompt3 = "How can I maintain focus better?"
response3 = manager.augmented_query(user_prompt3)
print(f"\nAssistant: {response3}")
```

