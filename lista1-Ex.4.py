# Como poderíamos tornar o programa da questão 3 mais genérico, de maneira que pudéssemos registrar qualquer questão obejetiva com 5 alternativas.
pergunta='Qual o verdadeiro nome do super-herói Batman?'
alternativaA='a)Bruce Wayne'
alternativaB='b)Clark Kent'
alternativaC='c)Peter Parker'
alternativaD='d)Tony Stark'
alternativaE='e)Steve Rogers'

print(pergunta)
print(alternativaA,alternativaB,alternativaC,alternativaD,alternativaE)

respostausuario=input('Digite sua resposta completa:')
print('Sua resposta foi:',respostausuario,'.' 'Resposta correta:',alternativaA,'.')

