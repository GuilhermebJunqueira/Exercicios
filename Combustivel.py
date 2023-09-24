
preco_gasolina = 3.30
preco_alcool = 2.90
limite_desconto = 20

litros_vendidos = float(input("Digite o número de litros vendidos: "))
tipo_combustivel = input("Digite o tipo de combustível (A para álcool, G para gasolina): ")


if tipo_combustivel == 'A' or tipo_combustivel == 'a':
    if litros_vendidos <= limite_desconto:
        valor_total = litros_vendidos * (preco_alcool - (0.03 * preco_alcool))
    else:
        valor_total = litros_vendidos * (preco_alcool - (0.05 * preco_alcool))
elif tipo_combustivel == 'G' or tipo_combustivel == 'g':
    if litros_vendidos <= limite_desconto:
        valor_total = litros_vendidos * (preco_gasolina - (0.04 * preco_gasolina))
    else:
        valor_total = litros_vendidos * (preco_gasolina - (0.06 * preco_gasolina))
else:
    print("Tipo de combustível inválido. Use 'A' para álcool ou 'G' para gasolina.")
    exit()

print(f"Valor a ser pago: R$ {valor_total:.2f}")
