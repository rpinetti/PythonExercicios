import random
# Desafio 025 - Crie um programa que leia o nome de uma pessoa e
#  diga se ela tem "SILVA" no nome

print('{:=^30}'.format(' DESAFIO 025 '))
nome = input('Digite seu nome: ')
print("O seu nome possui SILVA? {}".format("SILVA" in nome.upper()))
print('=' * 30)
