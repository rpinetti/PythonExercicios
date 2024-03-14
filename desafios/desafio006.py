print('{:=^30}'.format(' DESAFIO 006 '))
n = int(input('Digite um número: '))
print('Dobro: {}'.format(n * 2), end=' >>> ')
print('Triplo: {}'.format(n * 3), end=' >>> ')
#print('raíz quadrada: {}'.format(n ** (1/2)))  --> faltou formatar as casas decimais
print('raíz quadrada: {:.2f}'.format(n ** (1/2)))
print('=' * 30)
