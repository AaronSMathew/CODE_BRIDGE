# Python AI Projects

This repository contains two simple AI projects implemented in Python:

1. Rule-Based Chatbot
2. Tic-Tac-Toe AI using Minimax Algorithm

## 1. Rule-Based Chatbot

### Description
This is a simple rule-based chatbot that responds to user input based on predefined patterns and responses.

### Features
- Recognizes greetings, farewells, and common questions
- Uses regular expressions for pattern matching
- Provides a default response for unrecognized inputs

### How to Use
1. Run the `simple_chatbot.py` script:
   ```
   python simple_chatbot.py
   ```
2. Type your messages and see the chatbot's responses
3. Type 'bye' to exit the chat

### Implementation Details
- The chatbot uses a list of rules, each consisting of a regular expression pattern and a corresponding response
- It checks the user's input against each rule and returns the matching response
- If no rule matches, it returns a default response

## 2. Tic-Tac-Toe AI

### Description
This project implements a Tic-Tac-Toe game where a human player can play against an AI opponent that uses the Minimax algorithm.

### Features
- Human vs AI gameplay
- Unbeatable AI using Minimax algorithm
- Command-line interface

### How to Use
1. Run the `tictactoe_ai.py` script:
   ```
   python tictactoe_ai.py
   ```
2. Follow the prompts to make your moves
3. The board positions are numbered 0-8, starting from the top-left corner and moving right and down

### Implementation Details
- The game board is represented as a list of 9 elements
- The Minimax algorithm is used to determine the best move for the AI
- The AI evaluates all possible future game states to make its decision

## Requirements
- Python 3.x

## Future Improvements
- Add a graphical user interface for both projects
- Implement difficulty levels for the Tic-Tac-Toe AI
- Expand the chatbot's knowledge base and improve its natural language processing capabilities

Feel free to contribute to these projects or use them as a starting point for your own AI experiments!
