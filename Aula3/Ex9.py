def somente_digitos(texto):
	return "".join(caractere for caractere in texto if caractere.isdigit())


def telefone_valido(telefone):
	quantidade_digitos = len(somente_digitos(telefone))
	return quantidade_digitos in (10, 11)



print(telefone_valido("(49) 99999-0001"))
print(telefone_valido("49 3246-0000"))
print(telefone_valido("123"))
