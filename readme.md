# Pathfinding Algorithms

## Overview
This project implements and evaluates three different pathfinding algorithms:
- **Breadth-First Search (BFS)**
- **Greedy Best-First Search**
- **A* Search**

The goal is to find the shortest path from a starting position (`s`) to the goal (`D`) in ASCII maps while avoiding obstacles (`*`). 
The algorithms are tested on maps of increasing sizes: **300x300, 600x600, and 900x900**.

## Algorithms Explained
### 1. **Breadth-First Search (BFS)**
- Explores all possible paths evenly.
- Guaranteed to find the shortest path but is **computationally expensive**.
- Visits most cells, leading to a **high iteration count** and **longer execution time**.

### 2. **Greedy Best-First Search**
- Much **faster** than BFS but often finds **longer** paths.
- Doesn't guarantee the shortest path but greatly reduces iteration count.

### 3. **A* Search**
- Uses both the heuristic (like Greedy) and actual path cost (like BFS).
- Balances **efficiency and optimality** by reducing unnecessary exploration.
- Generally **faster than BFS** while still finding the shortest path.

---

## Experiment Results
The algorithms were tested on three maps: **300x300, 600x600, and 900x900**.

| **Map Size**  | **Algorithm** | **Path Length** | **Iterations** | **Execution Time (s)** |
|--------------|-------------|--------------|-------------|----------------|
| **300x300**  | BFS         | **555**      | 47233       | 0.1240  |
|              | Greedy      | **983**      | 3358        | 0.0123  |
|              | A*          | **555**      | 8202        | 0.0275  |
| **600x600**  | BFS         | **1248**     | 197804      | 0.5381  |
|              | Greedy      | **1974**     | 6293        | 0.0216  |
|              | A*          | **1248**     | 60472       | 0.2398  |
| **900x900**  | BFS         | **1844**     | 450414      | 1.4073  |
|              | Greedy      | **4130**     | 29496       | 0.1151  |
|              | A*          | **1844**     | 93999       | 0.4692  |

### **Observations:**
1. **BFS** finds the shortest path but takes the longest time due to high iterations.
2. **Greedy Search** is significantly faster but finds suboptimal, longer paths.
3. **A*** achieves the best balance, finding the optimal path like BFS but in much fewer iterations and less time.

---

## Conclusion
- **BFS** is useful for verifying shortest paths but is too slow for large maps.
- **Greedy Search** is great when speed is more important than optimality.
- **A*** is the best choice for **efficiency and shortest path accuracy**.

---
