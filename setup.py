from setuptools import setup, find_packages

setup(
    name='MetaFlow',
    version='0.1',
    packages=find_packages(),
    install_requires=[
        openai>=1.60.1
    ],
    description=(
        "No more chatbots that are either stupidly stubborn or annoyingly agreeable. "
        "A conversation manager that prompts your LLM to identify deep unconscious preferences "
        "in the user's cognition - and determine whether they are compatible with the user's "
        "perceived end goal. The LLM will then work to weaken any counter-productive unconscious "
        "preferences, while also addressing the prompt directly.\n\n"
        "Particularly useful in any context that requires even a modicum of emotional intelligence."
    ),
    author='TwinPhoenix1',
    author_email='ivaylo.e.ivanov@gmail.com',
    url='https://github.com/TwinPhoenix1/MetaFlow',
    python_requires='>=3.11'
)