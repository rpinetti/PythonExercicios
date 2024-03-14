###########################################################
## Operadores aritméticos ##
# + soma
# - subtração
# * multiplicação
# / divisão
# ** potênciação
# // divisão inteiro
# % resto da divisão

## Ordem de precedência ##
# 1- ()
# 2- **
# 3- * / // %
# 4- + -
###########################################################

total = 5 + 3 * 2
print(total)

total = 3 * 5 + 4 ** 2
print(total)

total = 3 * (5 + 4) ** 2
print(total)

pow(4, 3)           # função para potência -> ignora a ordem de precedência

n1 = int(input('Um valor: '))
n2 = int(input('Outro valor: '))
s = n1 + n2
su = n1 - n2
m = n1 * n2
d = n1 / n2
di = n1 // n2
rd = n1 % n2
e = n1 ** n2

print('A soma é {} \n a subtração é {}'.format(s, su))                  # /n quebra a linha
print('A multiplicação é {} e a divisão é {:.3f}'.format(m, d))     # formata com 3 casas decimais
print('A divisão inteira é {} e o resto é {}'.format(di, rd), end=' ')  # concatena os prints
print('A potência é {}'.format(e))

### Formatar saída
nome = input('Qual o seu nome?')
print('Prazer em te conhecer {:>20}!'.format(nome))
print('Prazer em te conhecer {:<20}!'.format(nome))
print('Prazer em te conhecer {:^20}!'.format(nome))
print('Prazer em te conhecer {:=^20}!'.format(nome))
print('=' * 20)     # replica a string 20 vezes