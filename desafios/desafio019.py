from random import choice

# Desafio 019 - Um professor quer sortear um dos seus quatro alunos para apagar o quadro.
# Faça um programa que ajude ele, lendo o nome deles e escrevendo o nome do escolhido.

lista = []
aluno = 0

print('{:=^30}'.format(' DESAFIO 019 '))
while aluno < 4:
    lista.append(input('Nome do aluno {}: '.format(aluno + 1)))
    aluno = aluno + 1
# escolhido = random.randint(0, 3)
escolhido = choice(lista)
print('O aluno escolhido foi o {}'.format(lista[escolhido]))
print('=' * 30)
