print('{:=^30}'.format(' DESAFIO 007 '))
n1 = float(input('Nota 1: '))
n2 = float(input('Nota 2: '))
media = (n1 + n2) / 2
#print('A média entre {} e {} é {:.1f}'.format(n1, n2, media))  --> faltou formatar as variáveis n1 e n2
print('A média entre {:.1f} e {:.1f} é {:.1f}'.format(n1, n2, media))
print('=' * 30)
