op = int(input("Digite 1- Região Norte 2- Região Nordeste 3- Região Centro-Oeste 4- Região Sul: "))
iv = int(input("Digite 1- Ida 2- Ida e Volta: "))

if op == 1:
    if iv == 1:
        print("O valor da passagem de ida para Região Norte: R$500.00")
    else:
        print("O valor da passagem de ida-volta para Região Norte: R$950.00")
elif op == 2:
    if iv == 1:
        print("O valor da passagem de ida para Região Nordeste: R$350.00")
    else:
        print("O valor da passagem de ida-volta para Região Nordeste: R$650.00")
elif op == 3:
    if iv == 1:
        print("O valor da passagem de ida para Região Centro-Oeste: R$350.00")
    else:
        print("O valor da passagem de ida-volta para Região Centro-Oeste: R$600.00")
elif op == 4:
    if iv == 1:
        print("O valor da passagem de ida para Região Sul: R$300.00")
    else:
        print("O valor da passagem de ida-volta para Região Sul: R$550.00")
else:
    print("Opção Inexistente")
