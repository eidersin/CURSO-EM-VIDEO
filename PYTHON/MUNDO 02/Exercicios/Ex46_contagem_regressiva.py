# Mundo 02: Exercício 46
"""
Faça um programa que mostra na tela uma contagem regressiva para o estouro de fogos de artificio indo de 10 até 0
com pausa de 1segundo entre elas.
"""
from time import sleep
for c in range(10, -1, -1):
    print(c)
    sleep(1)
print('FOGOS')