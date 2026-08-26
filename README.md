markdown_content = """# Python Notebooks for Differential Equations & Picard–Lindelöf Theorem

This repository contains 4 Jupyter Notebooks designed to help students learning **Differential Equations** get comfortable with **Python programming** and explore the **Picard–Lindelöf theorem**.

---

## 📚 What is inside this repository?

### 1. `3n+1.ipynb` — Collatz Conjecture
* **What it does:** You enter a positive whole number, and the program runs the Collatz rules ($3n + 1$ for odd numbers, $n / 2$ for even numbers) to print the sequence until it reaches **1**.
* **Why it helps:** A simple and fun introduction to basic Python loops (`while`), conditional statements (`if/else`), and sequence generation.

---

### 2. `Function.ipynb` — Prime Factorization
* **What it does:** Takes a natural number as input and breaks it down into its prime factors.
* **Why it helps:** Teaches how to write and use functions (`def`) in Python, as well as basic arithmetic and logical operations.

---

### 3. `Math Plot.ipynb` — Basic Matplotlib & Function Plotting
* **What it does:** Teaches step-by-step how to plot mathematical functions using the `matplotlib` library.
* **Why it helps:** Visualizing curves, direction fields, and function approximations is essential for understanding differential equations.

---

### 4. `Picard.ipynb` — Picard Iteration for 1st Order ODEs
* **What it does:** Implements the Picard iteration method step-by-step to compute successive approximations for solving first-order Ordinary Differential Equations (ODEs).
* **Why it helps:** Connects Python programming directly to the core theory of the **Picard–Lindelöf theorem** (existence and uniqueness of solutions to ODEs).

---

## 🛠️ Requirements

To run these notebooks, you will need:
* Python 3
* Jupyter Notebook or JupyterLab
* `matplotlib` library

You can install `matplotlib` using pip:
```bash
pip install matplotlib
