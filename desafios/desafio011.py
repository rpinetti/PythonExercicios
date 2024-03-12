print('{:=^30}'.format(' DESAFIO 011 '))
altura = float(input('Altura da parede: '))
largura = float(input('Largura da parede: '))
area = altura * largura
tinta = area / 2
print('Para pintar {}m2 de parede\nprecisa de {}L de tinta'.format(area, tinta))
print('=' * 30)
