markdown_content = """# Python Notebooks for Differential Equations & Picard–Lindelöf Theorem

This repository contains 4 Jupyter Notebooks designed to help students learning **Differential Equations** get comfortable with **Python programming** and explore the **Picard–Lindelöf theorem**.

---

## What is inside this repository?

### 1. `3n+1.ipynb` and `3n+1.py` &mdash; Collatz Conjecture
* **What it does:** You enter a positive whole number, and the program runs the Collatz rules ($3n + 1$ for odd numbers, $n / 2$ for even numbers) to print the sequence until it reaches **1**.
* **Why it helps:** A simple and fun introduction to basic Python loops (`while`), conditional statements (`if/else`), and sequence generation.
* There are two functions: `collatza` use a raw `while` loop until the output `1` is reached, while `collatzb` use recursive programming (self-call). On theory the latter should be faster, but in `__main__` of `3n+1.py`namespace I include the time measuring for both functions to see if this is the case. 

---

### 2. `Function.ipynb` and `Function.py` &mdash; Prime Factorization
* **What it does:** Takes a natural number as input and breaks it down into its prime factors.
* **Why it helps:** Teaches how to write and use functions (`def`) in Python, as well as basic arithmetic and logical operations (especially letting students know that they don't need to check for factor up to $n$, but only $\sqrt{n}$.

---

### 3. `Math Plot.ipynb` &mdash; Basic Matplotlib & Function Plotting
* **What it does:** Teaches step-by-step how to plot mathematical functions using the `matplotlib` library, including legend, title, axis labels.
* **Why it helps:** Visualizing curves, direction fields, and function approximations is essential for understanding differential equations.

---

### 4. `Picard.ipynb` &mdash; Picard Iteration for 1st Order ODEs
* **What it does:** Implements the Picard iteration method step-by-step to compute successive approximations for solving first-order Ordinary Differential Equations (ODEs).
* **Why it helps:** Connects Python programming directly to the core theory of the **Picard–Lindelöf theorem** (existence and uniqueness of solutions to ODEs).

---

### 5. `Plot.ipynb` &mdash; 1nd Order system of ODEs
* **What it does:** Provides examples of different *phase portraits* of linear systems of the form $A'=AX$ to understand how eigenvalues of $A$ impacts how the solution trajectories $(x(t), y(t))$ look on the $xy$-coordinates  
* **Why it helps:** Connects linear algebra with differential equations

---

## Requirements

To run these notebooks, you will need:
* Python 3
* Jupyter Notebook or JupyterLab
* `matplotlib` library

You can install `matplotlib` and `numpy` using pip:
```bash
pip install matplotlib numpy
```
