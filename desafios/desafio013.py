print('{:=^30}'.format(' DESAFIO 013 '))
salario = float(input('Salário do funcionário: '))
aumento = salario * ( 1 + 0.15 )
print('Com o aumento de 15%, o funcionário receberá R${:.2f}'.format(aumento))
print('=' * 30)
