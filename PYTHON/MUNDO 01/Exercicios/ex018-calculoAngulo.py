
# Exercício 18 – Seno, Cosseno e Tangente

print('====== Exercício 18 – Seno, Cosseno e Tangente')
from math import radians, sin, cos, tan

angulo = float(input('Digite o angulo a ser calculado: '))
seno = sin(radians(angulo))
cosseno = cos(radians(angulo))
tangente = tan(radians(angulo))

print('O seno é {:.2f}'.format(seno))
print('O cosseno é {:.2f}'.format(cosseno))
print('O tangente {:.2f}'.format(tangente))