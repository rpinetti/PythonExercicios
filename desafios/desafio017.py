from math import sqrt, hypot

# Desafio 017 - faça um programa que leia o comprimento do cateto oposto e do cateto adjacente
#  de um triângulo retângulo, calcule e mostre o comprimento da hipotenusa

print('{:=^30}'.format(' DESAFIO 017 '))
triangulo =  ' |\\ \n'
triangulo += ' | \\ \n'
triangulo += ' |  \\ \n'
triangulo += ' |   \\ \n'
triangulo += ' ------'
print(triangulo)

# cateto1 = int(input('Comprimento do cateto oposto: '))
# cateto2 = int(input('Comprimento do cateto adjacente: '))
cateto1 = float(input('Comprimento do cateto oposto: '))
cateto2 = float(input('Comprimento do cateto adjacente: '))
hipotenusa = sqrt(cateto1**2 + cateto2**2)
print('O comprimento da hipotenusa: {:.3f}'.format(hipotenusa))

print('\n{:-^30}'.format(' Opção 2 '))
print('Utilizando o método hypot')
hipotenusa = hypot(cateto1, cateto2)
print('O comprimento da hipotenusa: {:.3f}'.format(hipotenusa))
print('=' * 30)
