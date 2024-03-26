import random
# Desafio 023 - Faça um programa que leia um número de 0 a 9999 e
# mostre na tela cada um dos dígitos separados.
#
# Exemplo:
# Digite um número: 1984
# unidade: 4
# dezena: 8
# centena: 9
# milhar: 1

print('{:=^30}'.format(' DESAFIO 023 '))
numero = input('Digite um número de 0 a 9999: ')

print("\n" + "-" * 15)
print("String")
print("-" * 15)
# numero = numero.rjust(4, "0")
numero = numero.zfill(4)
print("unidade: {}".format(numero[3]))
print("dezena: {}".format(numero[2]))
print("centena: {}".format(numero[1]))
print("milhar: {}".format(numero[0]))

print("\n" + "-" * 15)
print("Número")
print("-" * 15)
inteiro = int(numero)
milhar = inteiro // 1000
inteiro = inteiro - milhar * 1000
centena = inteiro // 100
inteiro = inteiro - centena * 100
dezena = inteiro // 10
unidade = inteiro - dezena * 10
print("unidade: {}".format(unidade))
print("dezena: {}".format(dezena))
print("centena: {}".format(centena))
print("milhar: {}".format(milhar))
print('=' * 30)
