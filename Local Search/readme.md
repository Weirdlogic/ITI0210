# N-Queens Hill Climbing Solver

## Problem Description
The N-Queens problem is a classic optimization problem where the goal is to place N queens on an NxN chessboard such that no two queens can capture each other. This means that no two queens can share the same row, column, or diagonal.

## Approach
This implementation uses **Hill Climbing Search** with the following structure:
- The chessboard is represented as an array of size N. The value at each index represents the row position of a queen in that column.
- The value function calculates the number of conflicting queen pairs.
- The search begins with a random board configuration.
- The algorithm then finds the "best move" (a move that minimizes conflicts) and applies it.
- If no improving move is found, the search stops (local minimum).

### Why Hill Climbing?
Hill Climbing is a local search algorithm that efficiently finds solutions for small N-Queens problems. It is not guaranteed to always find a solution due to the risk of being stuck in local minima, but it is simple and fast.

## Usage
1. Set the value of N in the main block of the script (default is N=8).
2. Run the script with:
```bash
python n_queens_hill_climbing.py
```

## Example Results
- **N=4:** Typically solves in a few iterations, but sometimes fails.
- **N=8:** Often solves but may fail due to local minima.

### Example Runs:
#### N=4
Initial position: [2, 0, 3, 1]
Final position: [2, 0, 3, 1]
Final value: 0

#### N=8
Initial position: [5, 3, 3, 6, 6, 7, 4, 5]
Final position: [5, 0, 3, 6, 0, 7, 4, 1]
Final value: 2

## Success Rate
- For N=4, success rate: ~60% (sometimes gets stuck with 1-2 conflicts).
- For N=8, success rate: ~14% based on test results (1 out of 7 runs solved the problem).

## Test Observations
- The algorithm often gets stuck in local minima for both N=4 and N=8.
- These local minima have a small number of conflicts (1-2), but not zero.

## Limitations
- Hill Climbing without random restarts may get stuck in local minima.
- The current implementation does not use random restarts or simulated annealing.
