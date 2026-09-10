numero = int(input("Digite um número positivo: "))
par = 0
impar = 0

if numero < 0:
    print("número inválido, o número tem que ser positivo")
else:
    for i in range(1, numero + 1):
        if i % 2 ==0:
            par = par + 1
        if i % 2 != 0:
            impar = impar + 1
    print(f"a quantidade de numeros pares são: {par}")
    print(f"a quantidade de numeros ímpares são: {impar}")    