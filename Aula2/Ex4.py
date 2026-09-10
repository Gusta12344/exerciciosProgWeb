numero = int(input("Digite um número inteiro positivo: "))

if numero < 0:
    print("numero inválido, o numero tem q ser positivo")

else:
    soma = 0
    for i in range(1, numero + 1):
        soma = i
        soma2 = soma - 1
        print(f"{soma2} + {soma}")