print ("Digite -1 para encerrar o programa")
quantidadenotas=0
media = 0 

while True:
    numero = float(input("Digite a nota: "))
    if numero == -1:
        if quantidadenotas > 0:
            print(f"A média das notas é: {media/quantidadenotas:.2f}")
            print(f"A quantidade de notas digitadas foi: {quantidadenotas}")
        else:
            print("Nenhuma nota informada.")
        break
    else:
        quantidadenotas += 1
        media = media + numero