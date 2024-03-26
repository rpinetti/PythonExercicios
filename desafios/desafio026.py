import random
# Desafio 026 - Faça um programa que leia uma frase pelo teclado e mostre:
# 1-) Quantas vezes aparece a letra "A"
# 2-) Em qual posição ela aparece a primeira vez
# 3-) Em qual posição ela aparece a última vez

print('{:=^30}'.format(' DESAFIO 026 '))
frase = input('Digite uma frase: ')
print("Quantas vezes aparece a letra 'A'? {}".format(frase.upper().count("A")))
print("Em qual posição ela aparece a primeira vez? {}".format(frase.upper().lfind("A")))
print("Em qual posição ela aparece a última vez? {}".format(frase.upper().rfind("A")))
print('=' * 30)
