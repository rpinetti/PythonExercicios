print('{:=^30}'.format(' DESAFIO 008 '))
m = float(input('Tamanho em métros: '))
km = m / 1000
hm = m / 100
dam = m / 10
dm = m * 10
cm = m * 100
mm = m * 1000
print('A medida de {}m corresponda a: '.format(m))
print('{} Km'.format(km))
print('{} Hm'.format(hm))
print('{} Dam'.format(dam))
print('{} m'.format(m))
print('{} dm'.format(dm))
print('{:.0f} cm'.format(cm))   # Imprime sem as casa decimais
print('{:.0f} mm'.format(mm))   # Imprime sem as casa decimais
print('=' * 30)
