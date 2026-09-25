from Ex9 import somente_digitos


def formatar_telefone(telefone):
	digitos = somente_digitos(telefone)

	if len(digitos) == 11:
		return f"({digitos[:2]}) {digitos[2:7]}-{digitos[7:]}"
	if len(digitos) == 10:
		return f"({digitos[:2]}) {digitos[2:6]}-{digitos[6:]}"
	return telefone


print(formatar_telefone("49999990001"))
print(formatar_telefone("4932460000"))
print(formatar_telefone("123"))
