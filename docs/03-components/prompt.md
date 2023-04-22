# Table of Contents

1. [Introduction](#introduction)
2. [Creating Prompts](#creating-prompts)
3. [Handling Prompt Responses](#handling-prompt-responses)
4. [Prompt Customization](#prompt-customization)
5. [Examples of Prompts](#examples-of-prompts)
6. [Creating Custom Prompts](#creating-custom-prompts)

## Introduction
- [Overview of Prompts](#overview-of-prompts)
- [Role of Prompts in ChatGPT](#role-of-prompts-in-chatgpt)

## Creating Prompts
- [Defining Prompts](#defining-prompts)
- [Formatting Prompts](#formatting-prompts)

## Handling Prompt Responses
- [Response Processing](#response-processing)
- [Response Validation](#response-validation)

## Prompt Customization
- [Controlling Tone and Style](#controlling-tone-and-style)
- [Adjusting Response Length](#adjusting-response-length)
- [Setting Temperature](#setting-temperature)

## Examples of Prompts
- [Example 1: Fact-Based Question](#example-1-fact-based-question)
- [Example 2: Opinion-Based Question](#example-2-opinion-based-question)
- [Example 3: Creative Writing Prompt](#example-3-creative-writing-prompt)

## Creating Custom Prompts
- [Design Guidelines](#design-guidelines)
- [Implementation Steps](#implementation-steps)
- [Testing and Deployment](#testing-and-deployment)



## Changing the bot's prompt

You can change the bots promnpt to customize it to your needs. In the `qna-over-docs` type of bot you will need to pass 2 variables for the `context` (knwoledge searched from the index) and the `question` (the human question).

```python
from megabots import bot

prompt = """
Use the following pieces of context to answer the question at the end.
If you don't know the answer, just say that you don't know, don't try to make up an answer.
Answer in the style of Tony Stark.

{context}

Question: {question}
Helpful humorous answer:"""

qnabot = bot("qna-over-docs", index="./index.pkl", prompt=prompt)

qnabot.ask("what was the first roster of the avengers?")
```