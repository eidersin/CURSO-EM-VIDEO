# Mundo 02: Exercício 45
"""
Crie um programa que faça o computador jogar Jokenpô com você.

"""
from random import choice
from time import sleep
print('VAMOS JOGAR JOKENPô.\nSuas opções: ')
jogador = str(input('Pedra\nPapel\nTesoura\nQual é a sua jogada? ').strip().upper())
print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PO!!!')
print('-=-' * 10)

computador = choice(['PEDRA', 'PAPEL', 'TESOURA'])
if (jogador == 'PEDRA' and computador == 'PEDRA' or jogador == 'PAPEL' and computador == 'PAPEL' or jogador == 'TESOURA'
        and computador == 'TESOURA'):
    print('Você jogou {}'.format(jogador))
    print('O computador jogou {}'.format(computador))
    print('O resultado foi EMPATE')

elif (jogador == 'PAPEL' and computador == 'PEDRA' or jogador == 'PEDRA' and computador == 'TESOURA' or
      jogador == 'TESOURA' and computador == 'PAPEL'):
    print('Você jogou {}'.format(jogador))
    print('O computador jogou {}'.format(computador))
    print('-=-' * 10)
    print('JOGADOR VENCE')

else:
    print('Você jogou {}'.format(jogador))
    print('O computador jogou {}'.format(computador))
    print('-=-' * 10)
    print('COMPUTADOR VENCE!')
    