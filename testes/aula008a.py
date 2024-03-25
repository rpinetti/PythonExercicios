import emoji
import random
from math import sqrt, ceil, floor

print(emoji.emojize("Python é :polegar_para_cima:", language='pt'))

numero = random.randint(1, 100)
raiz = sqrt(numero)
print('A raíz de {} é {:.2f}'.format(numero, raiz))
print('Arredondar para mais: {}'.format(ceil(raiz)))
print('Arredondar para menos: {}'.format(floor(raiz)))