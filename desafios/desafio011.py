print('{:=^30}'.format(' DESAFIO 011 '))
largura = float(input('Largura da parede: '))
altura = float(input('Altura da parede: '))
area = altura * largura
print('Sua parede tem a dimensão de {} x {}m e sua área é de {}m2'.format(largura, altura, area))
tinta = area / 2
print('Para pintar {}m2 de parede\nprecisa de {}L de tinta'.format(area, tinta))
print('=' * 30)
