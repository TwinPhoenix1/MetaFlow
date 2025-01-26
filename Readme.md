# MetaFlow: Adaptive LLM Communication Through NLP Meta-Program Analysis  

**Enhance LLM interactions with unconscious preference detection and adaptive communication strategies**  

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

