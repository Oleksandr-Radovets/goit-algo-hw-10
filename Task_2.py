
import matplotlib.pyplot as plt
import numpy as np
from scipy.integrate import quad

def monte_carlo_integration():
    # Визначення функції та меж інтегрування
    def f(x):
        return x ** 2

    a = 0  # Нижня межа
    b = 2  # Верхня межа

    # Метод Монте-Карло для обчислення інтеграла
    N = 10000  # Кількість випадкових точок
    x_rand = np.random.uniform(a, b, N)
    y_rand = np.random.uniform(0, b**2, N)

    under_curve = y_rand < f(x_rand)
    integral_mc = (b * b**2) * (np.sum(under_curve) / N)

    # Аналітичний розрахунок інтеграла
    integral_quad, _ = quad(f, a, b)

    # Виведення результатів
    print(f"Інтеграл методом Монте-Карло: {integral_mc}")
    print(f"Аналітичне значення інтеграла: {integral_quad}")

    # Побудова графіка
    x = np.linspace(-0.5, 2.5, 400)
    y = f(x)
    fig, ax = plt.subplots()
    ax.plot(x, y, 'r', linewidth=2)
    ix = np.linspace(a, b)
    iy = f(ix)
    ax.fill_between(ix, iy, color='gray', alpha=0.3)
    ax.set_xlim([x[0], x[-1]])
    ax.set_ylim([0, max(y) + 0.1])
    ax.set_xlabel('x')
    ax.set_ylabel('f(x)')
    ax.axvline(x=a, color='gray', linestyle='--')
    ax.axvline(x=b, color='gray', linestyle='--')
    ax.set_title(f'Графік інтегрування f(x) = x^2 від {a} до {b}')
    plt.grid()
    plt.show()

if __name__ == "__main__":
    monte_carlo_integration()