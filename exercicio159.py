import math

def f(x):
    return (5 * x + 3) / math.sqrt(x**2 - 16)

x = float(input("Digite o valor de x: "))

if x > 4 and x < -4:
    fx = f(x)
    print(f"\nf(x) = {fx}")
else:
    print("\nNAO PODE SER FEITA")
