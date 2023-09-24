saldomedio = float(input("Digite o saldo médio: "))
credito = 0

if saldomedio < 501:
    credito = 0
else:
    if saldomedio < 1001:
        credito = saldomedio * 0.3
    else:
        if saldomedio < 3001:
            credito = saldomedio * 0.4
        else:
            credito = saldomedio * 0.5

if credito != 0:
    print(f"Como seu saldo era de: {saldomedio}, seu crédito será de: {credito}")
else:
    print(f"Como seu saldo era de: {saldomedio}, você não terá nenhum crédito")
