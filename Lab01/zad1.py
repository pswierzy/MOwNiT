import numpy as np
import matplotlib.pyplot as plt
import math

x = 1.0
tg_x = math.tan(x)
tg_x_prime = 1 + (math.tan(x))**2                       # f'(x)  
tg_x_prime_2 = 2 * tg_x * (1 + tg_x**2)                 # f''(x)
tg_x_prime_3 = 2 * (1 + tg_x**2) * (1 + 3 * tg_x**2)    # f'''(x)

eps = np.finfo(float).eps                               # Machine epsilon

h = np.array([10**(-k) for k in range(17)])

diff = (np.tan(x + h) - np.tan(x)) / h
comp_error = np.abs(diff - tg_x_prime)
trun_error = h * tg_x_prime_2 / 2
num_error = 2 * eps / h

plt.figure(figsize=(10, 6))
plt.loglog(h, comp_error, 'o-', label='Błąd całkowity')
plt.loglog(h, trun_error, '--', label='Błąd metody (obcięcia)')
plt.loglog(h, num_error, '--', label='Błąd obliczeniowy')
plt.xlabel('h (log)')
plt.ylabel('Błąd bezwzględny (log)')
plt.title('Analiza błędów: różnica progresywna')
plt.legend()
plt.grid(True, which='both', linestyle='--')
plt.show()

h_min = h[np.argmin(comp_error)]
h_min_theory = 2 * np.sqrt(eps / tg_x_prime_2)
print(f"Różnica progresywna:\n\th_min empiryczne: {h_min:.2e}\n\th_min teoretyczne: {h_min_theory:.2e}")


# 2 część

diff = (np.tan(x + h) - np.tan(x - h)) / (2 * h)
comp_error = np.abs(diff - tg_x_prime)
trun_error = tg_x_prime_3 * h ** 2 / 6
num_error = eps / h

plt.figure(figsize=(10, 6))
plt.loglog(h, comp_error, 'o-', label='Błąd całkowity')
plt.loglog(h, trun_error, '--', label='Błąd metody (obcięcia)')
plt.loglog(h, num_error, '--', label='Błąd obliczeniowy')
plt.xlabel('h (log)')
plt.ylabel('Błąd bezwzględny (log)')
plt.title('Analiza błędów: różnica centralna')
plt.legend()
plt.grid(True, which='both', linestyle='--')
plt.show()

h_min = h[np.argmin(comp_error)]
h_min_theory = (3 * eps / tg_x_prime_3) ** (1/3)
print(f"Różnica centralna:\n\th_min empiryczne: {h_min:.2e}\n\th_min teoretyczne: {h_min_theory:.2e}")