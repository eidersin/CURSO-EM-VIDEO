'''https://docs.python.org/pt-br/3/index.html Documentos do python

Trabalhando com Módulos

Biblioteca MATH
import math = importa todos
from math import 'item' = importa somente um item
   - Itens
   ceil = Arredondamento para cima
   floor = Arredondamento para baixo
   trunc = Elimina da virgula pra frente
   pow = Funçao potência (**)
   sqrt = Calcular Raiz quadrada
   factorial = Calcular fatorial

import math
from math import sqrt
num = eval(input('Digite um número: '))
raiz = sqrt(num)
print('A raiz de {} é igual a {:.2f}'.format(num, raiz))

import emoji
print(emoji.emojize('Olá, Mundo! \U0001f384'))'''