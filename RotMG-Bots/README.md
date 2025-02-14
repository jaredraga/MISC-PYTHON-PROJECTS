# RotMG Bots

## Overview
This repository contains various bots designed for the game Realm of the Mad God (RotMG). Each bot has its own functionality aimed at enhancing gameplay and automating tasks.

## Bots and Their Functionalities

### 1. Chat Bot
- **File:** `chat_bot.py`
- **Functionality:** Automates chat interactions in the game. Includes features for countdowns and random text generation.

### 2. Message Bot
- **File:** `rotmgMessageBot.py`
- **Functionality:** Automates daily quest retrieval and login processes for the game. It uses `pyautogui` to simulate mouse clicks and keyboard inputs for logging into the game, selecting servers, and navigating to quest rooms. The bot also incorporates optical character recognition (OCR) to read and parse in-game messages, allowing it to extract relevant information and make decisions based on the game state.

### 3. Name Generator
- **File:** `word_names.py`
- **Functionality:** Generates names by combining two words from a dictionary, ensuring the combined length does not exceed 10 letters. The bot loads words from a file and randomly selects two to create unique names. Furthermore, the bot uses machine learning algorithms to analyze the generated names and filter out those that are unlikely to be accepted by the game, increasing the chances of creating valid and usable names.

### 4. Auto Login Bot
- **File:** `rotmg-autologin`
- **Functionality:** Automates the login process for ROTMG, including handling multiple accounts and logging the activated accounts. It uses image recognition to find buttons and fields on the screen and inputs credentials automatically. The bot also employs encryption techniques to securely store and retrieve account credentials, ensuring the safety and security of user data.

### 5. White Bag Tester
- **File:** `whiteTester.py`
- **Functionality:** Tests the probability of acquiring a white bag in the game, tracking the number of runs and luck statistics. It simulates multiple runs to determine the likelihood of obtaining rare items and logs the results. Additionally, the bot uses statistical analysis to identify trends and patterns in the game's drop rates, providing valuable insights for players seeking to optimize their gameplay experience.