import random
# Desafio 024 - Crie um programa que leia o nome de uma cidade e
#  diga se ela começa com ou não com o nome "SANTO"

print('{:=^30}'.format(' DESAFIO 024 '))
cidade = input('Digite o nome da cidade: ')
print("O nome da cidade começa com SANTO? {}".format("SANTO" in cidade.upper()[:6]))
print('=' * 30)
