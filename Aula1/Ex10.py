print("======================================")
print("Conversor De Moedas")
print("======================================")
print("Escolha a moeda que deseja converter:")
print("1 - Real para Dólar")
print("2 - Dolar para Real")

escolha = int(input("Digite sua escolha (1 ou 2): "))
if escolha == 1:
    real = float(input("Digite o valor em reais: "))
    dolar = float(real / 5.40)
    print(f"O valor em dólares é: {dolar:.2f}")
elif escolha == 2:
    dolar = float(input("Digite o valor em dólares: "))
    real = float(dolar * 5.40)
    print(f"O valor em reais é: {real:.2f}")
else:
    print("Opção inválida. Por favor, escolha 1 ou 2.")