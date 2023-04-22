# Table of Contents

1. [Introduction](#introduction)
2. [Customizing Prompts](#customizing-prompts)
3. [Customizing Memory Modules](#customizing-memory-modules)
4. [Customizing Vector Store Modules](#customizing-vector-store-modules)
5. [Customizing UI Components](#customizing-ui-components)
6. [Customizing Agents](#customizing-agents)
7. [Customizing Multi-Agent Systems](#customizing-multi-agent-systems)

## Introduction
- [Overview of Customization](#overview-of-customization)
- [Getting Started with Customization](#getting-started-with-customization)

## Customizing Prompts
- [Adjusting Prompt Parameters](#adjusting-prompt-parameters)
- [Creating Custom Prompts](#creating-custom-prompts)

## Customizing Memory Modules
- [Memory Configuration Options](#memory-configuration-options)
- [Creating Custom Memory Modules](#creating-custom-memory-modules)

## Customizing Vector Store Modules
- [Vector Store Configuration Options](#vector-store-configuration-options)
- [Creating Custom Vector Store Modules](#creating-custom-vector-store-modules)

## Customizing UI Components
- [UI Customization Options](#ui-customization-options)
- [Creating Custom UI Components](#creating-custom-ui-components)

## Customizing Agents
- [Agent Customization Options](#agent-customization-options)
- [Creating Custom Agents](#creating-custom-agents)

## Customizing Multi-Agent Systems
- [Multi-Agent System Customization Options](#multi-agent-system-customization-options)
- [Creating Custom Multi-Agent Systems](#creating-custom-multi-agent-systems)

## Customising bot

The `bot` function should serve as the starting point for creating and customising your bot. Below is a list of the available arguments in `bot`.

| Argument    | Description                                                                                                                                                                                                                                                                                |
| ----------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| task        | The type of bot to create. Available options: `qna-over-docs`. More comming soon                                                                                                                                                                                                           |
| index       | Specifies the index to use for the bot. It can either be a saved index file (e.g., `index.pkl`) or a directory of documents (e.g., `./index`). In the case of the directory the index will be automatically created. If no index is specified `bot` will look for `index.pkl` or `./index` |
| model       | The name of the model to use for the bot. You can specify a different model by providing its name, like "text-davinci-003". Supported models: `gpt-3.5-turbo` (default),`text-davinci-003` More comming soon.                                                                              |
| prompt      | A string template for the prompt, which defines the format of the question and context passed to the model. The template should include placeholder variables like so: `context`, `{question}` and in the case of using memory `history`.                                                  |
| memory      | The type of memory to be used by the bot. Can be a string with the type of the memory or you can use `memory` factory function. Supported memories: `conversation-buffer`, `conversation-buffer-window`                                                                                    |
| vectorstore | The vectorstore to be used for the index. Can be a string with the name of the databse or you can use `vectorstore` factory function. Supported DBs: `milvus`.                                                                                                                             |

| sources | When `sources` is `True` the bot will also include sources in the response. A known [issue](https://github.com/hwchase17/langchain/issues/2858) exists, where if you pass a custom prompt with sources the code breaks. |