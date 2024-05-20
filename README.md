# Newton-Raphson Method Implementation

This repository contains a Python implementation of the Newton-Raphson method for finding the root of a given function. The function used in this implementation is \( f(x) = 4x^3 - 15x^2 + 17x - 16 \).

## Overview

The Newton-Raphson method is an iterative numerical technique for finding approximate solutions to equations of the form \( f(x) = 0 \). This implementation includes the main algorithm, a function to compute the derivative of \( f(x) \), and a plotting function to visualize the iterations.

### Files

- main.py: Contains the implementation of the Newton-Raphson method and the plotting functions.

### Usage

1. Clone the repository:
   ```phyton
   git clone <repository-url>
   cd <repository-directory>
   ```
3. Run the program:
   ```phyton
   python main.py
   ```

5. Input: When prompted, enter an initial guess for the root.

## Functions

f(x)
Defines the function for which the root is to be found.
```python
def f(x):
    return 4 * x**3 - 15 * x**2 + 17 * x - 16
```

f_derivative(x)
Defines the derivative of the function \( f(x) \).
```python
def f_derivative(x):
    return 12 * x**2 - 30 * x + 17
```

newtonRaphson(x0)
Implements the Newton-Raphson method.
- Parameters: x0 (float) - initial guess.
- Returns: root (float) - estimated root, x_values (list of float) - x values of each iteration, y_values (list of float) - corresponding y values.
```python
def newtonRaphson(x0):
    # Implementation details
    return root, x_values, y_values
```

plot_function_and_iterations(x_values, y_values)
Plots the function and the iterations of the Newton-Raphson method.
- Parameters: x_values (list of float) - x values of each iteration, y_values (list of float) - corresponding y values.
```python
def plot_function_and_iterations(x_values, y_values):
    # Implementation details
```

## Example Output

Upon running the program, the user is prompted to input an initial guess. The program then iteratively applies the Newton-Raphson method, printing each iteration's value and finally plotting the function along with the iterations.

### Masukkan tebakan awal: 2
Iterasi ke-0: x = 2.0
Iterasi ke-1: x = 1.75
Iterasi ke-2: x = 1.6104651162790698
...
Akar persamaan adalah: 1.528013758419482

The plot will show the function \( f(x) \) and the iterations of the Newton-Raphson method.

## Requirements

- Python 3.x
- NumPy
- Matplotlib

Install the required packages using:
```python
pip install numpy matplotlib
```
