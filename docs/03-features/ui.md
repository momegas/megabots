# Table of Contents

1. [Introduction](#introduction)
2. [UI Components](#ui-components)
3. [UI Customization](#ui-customization)
4. [Examples of UI Designs](#examples-of-ui-designs)
5. [Creating Custom UI Components](#creating-custom-ui-components)

## Introduction
- [Overview of User Interface (UI)](#overview-of-user-interface)
- [Role of UI in ChatGPT](#role-of-ui-in-chatgpt)

## UI Components
- [Input Components](#input-components)
- [Output Components](#output-components)
- [Navigation Components](#navigation-components)

## UI Customization
- [Styling and Themes](#styling-and-themes)
- [Layout Customization](#layout-customization)
- [Accessibility](#accessibility)

## Examples of UI Designs
- [Example 1: Minimalist Design](#example-1-minimalist-design)
- [Example 2: Conversational UI](#example-2-conversational-ui)
- [Example 3: Dashboard UI](#example-3-dashboard-ui)

## Creating Custom UI Components
- [Design Guidelines](#design-guidelines)
- [Implementation Steps](#implementation-steps)
- [Testing and Deployment](#testing-and-deployment)



## Exposing a Gradio chat-like interface

You can expose a gradio UI for the bot using `create_interface` function.
Assuming your file is called `ui.py` run `gradio qnabot/ui.py` to run the UI locally.
You should then be able to visit `http://127.0.0.1:7860` to see the API documentation.

```python
from megabots import bot, create_interface

demo = create_interface(bot("qna-over-docs"))
```
