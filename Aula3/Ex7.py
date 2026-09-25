def media(a, b, c):
	return (a + b + c) / 3


def situacao(nota):
	if nota >= 7:
		return "aprovado"
	if nota >= 5:
		return "recuperação"
	return "reprovado"


def situacao_aluno(nota1, nota2, nota3):
	return situacao(media(nota1, nota2, nota3))


print(situacao_aluno(8, 7, 9))
print(situacao_aluno(5, 6, 4))
print(situacao_aluno(3, 4, 2))
