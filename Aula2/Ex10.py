import random

secreto = random.randint(1, 100)
tentativas = 0

while True:
    palpite = int(input("Digite um número entre 1 e 100: "))
    tentativas += 1

    if palpite < secreto:
        print("O número secreto é maior.")
    elif palpite > secreto:
        print("O número secreto é menor.")
    else:
        print(f"boa Você acertou o número secreto em {tentativas} tentativas.")
        break