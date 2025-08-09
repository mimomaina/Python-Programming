# Snakes and Ladders Game

A classic turn-based board game implemented in Python for 1 to 4 players. Players roll a dice, move across a 10x10 board, climb ladders, slide down snakes, and race to reach the final position (100) to win.

## Table of Contents

- [Overview](#overview)
- [Features](#features)
- [Game Rules](#game-rules)
- [Installation](#installation)
- [Usage](#usage)
- [How It Works](#how-it-works)
- [Board Layout](#board-layout)
- [Functions](#functions)
- [Sample Gameplay](#sample-gameplay)
- [License](#license)

## Overview

This Python script implements the classic Snakes and Ladders game using a 10x10 board (positions 1 to 100). The game supports 1 to 4 players who take turns rolling a dice, moving across the board, and navigating snakes and ladders. The first player to reach position 100 wins.

The game logic is built using the random module for dice rolls and structured functions to manage player movement, position updates, and win detection.

## Features

- Supports 1 to 4 players with custom names
- Interactive turn-based gameplay
- Dice rolling with feedback
- Automatic snake and ladder detection
- Position tracking and game status messages
- Win detection and game termination
- Input validation and error handling
- Clear game rules and instructions

## Game Rules

1. All players start at position 0.
2. Players take turns rolling a six-sided dice (values 1–6).
3. Move forward the number of spaces shown on the dice.
4. If you land at the bottom of a ladder, climb up to the top.
5. If you land on the head of a snake, slide down to the tail.
6. The first player to reach exactly 100 wins the game.
7. Press Enter to roll the dice on your turn.
8. Game supports 1 to 4 players (must enter valid number and names).
9. If a roll would take a player beyond position 100, they stay in their current position.

## Installation

### Prerequisites

- Python 3.6 or higher

### Setup

1. Save the code to a file:
   ```bash
   touch snakes_and_ladders.py
