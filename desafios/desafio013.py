print('{:=^30}'.format(' DESAFIO 012 '))
salario = float(input('Salário do funcionário: '))
aumento = salario * ( 1 + 0.15 )
print('O funcionário receberá R${:.2f}'.format(aumento))
print('=' * 30)