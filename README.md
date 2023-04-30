# ai-to-ia-poc

## Overview

This project is part of Encora's Generative AI Initiative. The initiative is meant to explore the use of Generative AI tools (e.g. ChatGPT, Claude, GitHub's Copilot X, Midjourney, etc.) for work during the SDLC. The AI to IA proof of concept is one of several PoCs for the Implementation phase of the SDLC, and it focuses on the writing, debugging and refactoring of code that takes place during that phase.

## Objective

This PoC will try to replicate the effects on productivity reported by GitHub and Microsot Research as presented in ['Productivity Assessment of Neural Code Completion'](https://arxiv.org/abs/2205.06537) by Albert Ziegler, Eirini Kalliamvakou, Shawn Simister, Ganesh Sittampalam, Alice Li, Andrew Rice, Devon Rifkin and Edward Aftandilian, a less technical overview of which can be read here: [Research: quantifying GitHub Copilot’s impact on developer productivity and happiness](https://github.blog/2022-09-07-research-quantifying-github-copilots-impact-on-developer-productivity-and-happiness/). Our objective is to verify an overall productivity improvement in the range of 35% to 40%.

## Methodology

Like GitHub and Microsoft Research we use the [SPACE framework](https://queue.acm.org/detail.cfm?id=3454124) to measure developer productivity.

## Tools

The project uses the following tech stack:

* Generative AI tools: Copilot, ChatGPT (GPT-4) and (optionally) Claude.
* Language: Python v3.11.x.
* IDE: Visual Studio Code v1.77.0+. Extensions: `Python` (from Microsoft), `Pylint`, `Black Formatter` (from Microsoft).
* Virtual environments/package management: `pipenv`.
* Code quality: 
  * Linting: `pylint`. 
  * Formatting: `black`.
  * Security: `bandit`. 
