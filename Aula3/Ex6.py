def contar_vogais(texto):
	vogais = "aeiouáéíóúâêôãõ"
	return sum(1 for caractere in texto.lower() if caractere in vogais)

texto = input("Digite um texto: ")
print(contar_vogais(texto))
