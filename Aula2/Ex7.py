numero = 0 
numeroatual = 0

for i in range(1, 6):
    numero = float(input(f"Digite o {i} número: "))
    if numero >= numeroatual:
        numeroatual = numero
print(f"O maior número digitado foi: {numeroatual}")