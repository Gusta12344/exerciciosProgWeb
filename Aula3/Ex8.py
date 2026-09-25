def apresentar(nome, cidade, uf="SC"):
	return f"{nome}, de {cidade}/{uf}"


print(apresentar("Ana", "Fraiburgo"))
print(apresentar("Ana", "Fraiburgo", "PR"))
print(apresentar("Ana", "Fraiburgo", uf="RS"))
