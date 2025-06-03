# 8-queens-problem

This project provides two different approaches to solve the classic **8 Queens Problem**, where the goal is to place 8 queens on an 8×8 chessboard such that no two queens threaten each other.

## 📂 Contents

- `back_tracking.py`: Solve using **backtracking** (with optional animation).
- `Genetic_algorithm.py`: Solve using a **genetic algorithm** (evolution-based).
- `back_tracking_animation.py`: Backtracking solution with **step-by-step visualization** using `matplotlib`.

---

## 🧬 1. Genetic Algorithm

The genetic algorithm version simulates evolution to gradually approach valid solutions.

### Features
- Population-based search
- Fitness function based on queen conflicts
- Mutation and selection over generations

### Usage

```bash
python Genetic_algorithm.py
```

## ♟️ 2. Backtracking Algorithm
This is a classical depth-first search approach with pruning (checking conflicts before placing).

Features
Guaranteed all 92 solutions

Efficient pruning for early failure

Option to visualize the solving process

```bash
python back_tracking.py
```
