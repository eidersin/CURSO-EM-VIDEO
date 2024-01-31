# Mundo 02: Exercício 68
"""
Fraça um programa que jogue par ou impar com o computador. O jogo só sera interrompido quando o jogador PERDER.
no final mostre o total de vitórias consecutivas que ele conquistou no final do jogo.
"""

# CÓDIGO FEITO POR MIM
from random import randint

vitoria = 0
while True:
    jogador = int(input('Diga um valor: '))
    computador = int(randint(1, 10))
    jogada = str(input('Par ou Impar? [P/I]')).upper().strip()[0]
    soma = jogador + computador
    if jogada in 'P':
        if soma % 2 == 0:
            print(50*'-')
            print(f'Você jogou {jogador} e o computador {computador}. Total de {soma} DEU PAR')
            print(50*'-')
            print('Você VENCEU')
            print('Vamos jogar novamente...')
            print(25*'=-')
            vitoria += 1
        else:
            print(50*'-')
            print(f'Você jogou {jogador} e o computador {computador}. Total de {soma} DEU ÍMPAR')
            print(50*'-')
            print('Você PERDEU!')
            print(25*'=-')
            break
    else:
        if soma % 2 != 0:
            print(20*'-')
            print(f'Você jogou {jogador} e o computador {computador}. Total de {soma} DEU IMPAR')
            print(20*'-')
            print('Você VENCEU')
            print('Vamos jogar novamente...')
            print(25*'=-')
            vitoria += 1
        else:
            print(50*'-')
            print(f'Você jogou {jogador} e o computador {computador}. Total de {soma} DEU PAR')
            print(50*'-')
            print('Você PERDEU!')
            print(25*'=-')
            break
print(f'GAME OVER! Você venceu {vitoria} vezes.')

# CÓDIGO FEITO PELA IA
"""from random import randint

def resultado(jogador, computador, soma, resultado):
    print(50*'-')
    print(f'Você jogou {jogador} e o computador {computador}. Total de {soma} DEU {resultado}')
    print(50*'-')

vitoria = 0
while True:
    jogador = int(input('Diga um valor: '))
    computador = randint(1, 10)
    jogada = str(input('Par ou Impar? [P/I]')).upper()
    soma = jogador + computador
    if (soma % 2 == 0 and jogada == 'P') or (soma % 2 != 0 and jogada == 'I'):
        resultado(jogador, computador, soma, 'PAR' if soma % 2 == 0 else 'ÍMPAR')
        print('Você VENCEU')
        print('Vamos jogar novamente...')
        print(25*'=-')
        vitoria += 1
    else:
        resultado(jogador, computador, soma, 'PAR' if soma % 2 == 0 else 'ÍMPAR')
        print('Você PERDEU!')
        print(25*'=-')
        break
print(f'GAME OVER! Você venceu {vitoria} vezes.')
"""