# Newton Raphson
import numpy as np
import matplotlib.pyplot as plt

# Toleransi error
EPSILON = 1e-13

# Fungsi yang akan dicari akarnya
def f(x):
    return 4*x**3 - 15*x**2 + 17*x - 16

# Turunan dari fungsi f(x)
def f_derivative(x):
    return 12*x**2 - 30*x + 17

# Implementasi metode Newton-Raphson
def newtonRaphson(x0):
    h = f(x0) / f_derivative(x0)
    iter_count = 0  # Untuk menghitung jumlah iterasi
    
    print(f"Iterasi ke-{iter_count}: x = {x0}, f(x) = {f(x0)}")
    x_values = [x0]
    y_values = [f(x0)]
    
    while abs(h) >= EPSILON:
        h = f(x0) / f_derivative(x0)
        x0 = x0 - h
        iter_count += 1
        print(f"Iterasi ke-{iter_count}: x = {x0}, f(x) = {f(x0)}")
        x_values.append(x0)
        y_values.append(f(x0))
    
    return x0, x_values, y_values

def plot_function_and_iterations(x_values, y_values):
    # Menentukan rentang x untuk plot
    x = np.linspace(min(x_values) - 1, max(x_values) + 1, 400)
    y = f(x)
    
    plt.figure(figsize=(10, 6))
    plt.plot(x, y, label='f(x) = 4x^3 - 15x^2 + 17x - 16', color='blue')
    
    # Plotting iterasi Newton-Raphson
    plt.scatter(x_values, y_values, color='red')
    for i in range(len(x_values)):
        plt.text(x_values[i], y_values[i], f'({i})', fontsize=12, ha='right')
    
    plt.axhline(0, color='black', linewidth=0.5)
    plt.axvline(0, color='black', linewidth=0.5)
    plt.grid(color='gray', linestyle='-', linewidth=0.5)
    plt.title('Metode Newton-Raphson')
    plt.xlabel('x')
    plt.ylabel('f(x)')
    plt.legend()
    plt.show()

if __name__ == "__main__":
    x0 = float(input("Masukkan tebakan awal: "))
    root, x_values, y_values = newtonRaphson(x0)
    print(f"Akar persamaan adalah: {root}")
    plot_function_and_iterations(x_values, y_values)
