from math import modf, trunc

# Desafio 016 - Criar um programa que leia um número Real qualquer pelo teclado
# e mostre na tela a sua porção inteira

print('{:=^30}'.format(' DESAFIO 016 '))
numero = float(input('Informe um número real: '))
parteDecimal, parteInteira = modf(numero)
print('Parte inteira: {}'.format(parteInteira))
print('Parte decimal: {}'.format(parteDecimal))

print('\n{:-^30}'.format(' Opção 2 '))
print('Utilizando o método trunc')
print('O número digitado foi {} e a parte inteira é {}'.format(numero, trunc(numero)))

print('\n{:-^30}'.format(' Opção 3 '))
print('Utilizando a conversão para int')
print('O número digitado foi {} e a parte inteira é {}'.format(numero, int(numero)))

print('=' * 30)