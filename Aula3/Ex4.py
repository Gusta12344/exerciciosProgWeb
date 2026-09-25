def maior_de_tres(a, b, c):
	maior = a

	if b > maior:
		maior = b
	if c > maior:
		maior = c

	return maior


print(maior_de_tres(9, 4, 2))
print(maior_de_tres(4, 9, 2))
print(maior_de_tres(4, 2, 9))
