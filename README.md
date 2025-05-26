# ♛ N-Queens Solver with Particle Swarm Optimization (PSO)

This project solves the **N-Queens problem** using the **Particle Swarm Optimization (PSO)** algorithm, and visualizes the result using a simple **Tkinter GUI** in Python.

---

## 📌 Overview

The N-Queens problem challenges us to place `N` queens on an `N×N` chessboard such that no two queens attack each other. This implementation uses a heuristic approach based on PSO, which is inspired by the collective behavior of birds flocking or fish schooling.

---
## ⚙️ How It Works

- Each **particle** represents a possible queen placement (one per row).
- The **fitness function** counts the number of attacking queen pairs.
- Particles update their positions and velocities based on:
  - Their own best-known positions (`pBest`)
  - The best-known position of the swarm (`gBest`)
- The algorithm iterates until it finds a valid solution or hits a max number of iterations.

---

## 🧪 Example Output

```bash
Iteration 17: gBest = [1, 3, 5, 7, 2, 0, 6, 4], Conflits = 0
Solution trouvée avec 0 conflits.
Solution finale : [1, 3, 5, 7, 2, 0, 6, 4]
Conflits finaux : 0
