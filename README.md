# 8-Puzzle AI Agent

This repository contains an 8-Puzzle AI Solver implemented using various search algorithms including Depth-First Search (DFS), Breadth-First Search (BFS), Iterative Deepening Depth-First Search (IDFS), and A* Search. The project also includes a graphical user interface (GUI) built with PyQt5 to visualize the puzzle and the solution steps.

## Project Structure
```
/8-Puzzle-AI-Agent
│
├── Code
│   ├── AStar.py
│   ├── BFS.py
│   ├── dfs.py
│   ├── Iterative_dfs.py
│   ├── gui.py
│   ├── steps.py
│
├── .gitignore
├── LICENSE
├── README.md
```

## Files Description

- `AStar.py`: Contains the implementation of the A* search algorithm.
- `BFS.py`: Contains the implementation of the Breadth-First Search (BFS) algorithm.
- `dfs.py`: Contains the implementation of the Depth-First Search (DFS) algorithm.
- `Iterative_dfs.py`: Contains the implementation of the Iterative Deepening Depth-First Search (IDFS) algorithm.
- `gui.py`: Contains the implementation of the graphical user interface (GUI) using PyQt5.
- `steps.py`: Contains the implementation of the steps window to display the solution steps.

## Installation

1. Clone the repository:
    ```sh
    git clone https://github.com/ranimeshehata/8-Puzzle-AI-Agent.git
    cd 8-Puzzle-AI-Solver/Code
    ```

2. Install the required packages:
    ```sh
    pip install PyQt5
    ```

## Usage

To run the 8-Puzzle AI Solver, execute the following command:
```sh
python gui.py