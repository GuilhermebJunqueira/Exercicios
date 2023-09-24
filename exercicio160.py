x = float(input("Digite o valor de x: "))

if x <= 1:
    y = 1
elif 1 < x <= 2:
    y = 2.5
elif 2 < x <= 3:
    y = x ** 2
else:
    y = x ** 3

print(f"Valor de f(x): {y}")
