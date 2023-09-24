peso = float(input("Digite o peso: "))
altura = float(input("Digite a altura: "))

imc = peso / (altura ** 2)

if imc < 20:
    print("Abaixo do peso")
else:
    if imc <= 25:
        print("Normal")
    else:
        if imc <= 30:
            print("Excesso de peso")
        else:
            if imc <= 35:
                print("Obesidade")
            else:
                print("Obesidade mórbida")
