import random
# Desafio 027 - Faça um programa que leia o nome completo de uma pessoa,
#  mostrando em seguida o primeiro e o último nome separadamente
#
# Exemplo: Ana Maria de Souza
# primeiro = Ana
# último = Souza

print('{:=^30}'.format(' DESAFIO 027 '))
nome = input('Digite seu nome: ')
separar = nome.split()
print("primeiro = {}".format(separar[0]))
print("último = {}".format(separar[len(separar) - 1]))
print('=' * 30)
