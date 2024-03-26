import random
# Desafio 022 - CRie um programa que leia o nome completo de uma pessoa e mostre:
# 1-) O nome com todas as letras maiúsculas
# 2-) O nome com todas as letras minúsculas
# 3-) Quantas letras no total sem contar os espaços
# 4-) Quantas letras tem o primeiro nome

print('{:=^30}'.format(' DESAFIO 022 '))
nome = input('Digite seu nome: ')
print(nome.upper())
print(nome.lower())

qtdCaracteres = len(nome) - nome.count(" ")
print("Quantidade de caracteres sem o espaco: {}".format(qtdCaracteres))

separar = nome.split()
print("Quantidade de caracteres no primeiro nome: {}".format(len(separar[0])))

print('=' * 30)
