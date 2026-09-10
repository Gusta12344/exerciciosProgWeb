n1 = int(input("Digite a primeira nota: "))
n2 = int(input("Digite a segunda nota: "))
n3 = int(input("Digite a terceira nota: "))
media = (n1 + n2 + n3) / 3
print (f"A média das notas é: {media:.2f}")

if media >=7:
    print("Aprovado")
elif media >=4 and media <7:
    print("Recuperação")
else:
    print("Reprovado")