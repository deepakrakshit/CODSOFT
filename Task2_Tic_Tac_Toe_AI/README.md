# Task 2 – Tic-Tac-Toe AI

## Objective

Implement an AI agent that plays the classic game of Tic-Tac-Toe against a human player. The project utilizes the Minimax algorithm to evaluate all possible game states, resulting in an unbeatable AI opponent.

## Technologies Used

- Python 3
- math (Built-in Python module)

## Features

- Command-line game interface
- Human vs Computer gameplay
- Input validation and error handling
- Win and draw detection
- Unbeatable AI using the recursive Minimax algorithm
- Depth-scoring mechanism (forces the AI to win in the fewest moves possible)

## Project Structure

```text
Task2_Tic_Tac_Toe_AI/
│
├── tic_tac_toe.py
└── README.md
```

## How to Run

```bash
python tic_tac_toe.py
```

## Sample Conversation

```text
Welcome to Tic-Tac-Toe!
You are 'X' and you are playing against the Unbeatable Minimax AI ('O').

   |   |   
---+---+---
   |   |   
---+---+---
   |   |   

Enter your move (1-9): 5

   |   |   
---+---+---
   | X |   
---+---+---
   |   |   

AI is calculating the optimal move...

 O |   |   
---+---+---
   | X |   
---+---+---
   |   |   

Enter your move (1-9): 
```

## Future Improvements

- Alpha-Beta Pruning for performance optimization
- Graphical User Interface (GUI)
- Adjustable difficulty levels (e.g., toggling between Random AI and Minimax AI)
- Player vs Player mode toggle
- Score tracking across multiple rounds

## Author

**Deepak Rakshit**
Developed as part of the **CodSoft Artificial Intelligence Internship**.