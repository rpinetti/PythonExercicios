import random
# Desafio 020 - O mesmo professor quer sortear a ordem de apresentação dos trabalhos dos alunos.
# Faça um programa que leia o nome dos 4 alunos e mostre a ordem sorteada.

lista = []
aluno = 0

print('{:=^30}'.format(' DESAFIO 020 '))
while aluno < 4:
    lista.append(input('Nome do aluno {}: '.format(aluno + 1)))
    aluno = aluno + 1

novaLista = random.sample(lista, k=len(lista))

print('Ordem das apresentações')
for nome in novaLista:
    print(nome)

print('\n{:-^30}'.format(' Opção 2 '))
random.shuffle(lista)
print(lista)
print('=' * 30)
