print('{:=^30}'.format(' DESAFIO 010 '))
real = float(input('Quantos dinheiro você tem na carteira? R$'))
# dolar = real * 3.27   # errei o operador
dolar = real / 3.27
# print('Você pode comprar US$ {:.2f}'.format(dolar))   # outro tipo de mensagem
print('Com R${:.2f} você pode comprar US$ {:.2f}'.format(real, dolar))
print('=' * 30)
