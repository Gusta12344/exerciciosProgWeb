soma = 0

for i in range(5):
    numero = float(input(f"Digite o {i + 1} número: "))
    soma += numero

media = soma / 5

print(f"A soma dos números é: {soma:.2f}")
print(f"A média dos números é: {media:.2f}")