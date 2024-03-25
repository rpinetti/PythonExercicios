from math import radians, sin, cos, tan
import math

# Desafio 018 - faça um programa que leia um ângulo qualquer e mostre na tela o valor
#  do seno, cosseno e tangente desse ângulo

print('{:=^30}'.format(' DESAFIO 018 '))
# angulo = int(input('Informe um ângulo º: '))
angulo = float(input('Informe um ângulo º: '))
radiano = math.radians(angulo)
seno = math.sin(radiano)
cosseno = math.cos(radiano)
tangente = math.tan(radiano)
print('Radiano = {}'.format(radiano))
print('Seno = {}'.format(seno))
print('Cosseno = {}'.format(cosseno))
print('Tangente = {}'.format(tangente))
print('=' * 30)
