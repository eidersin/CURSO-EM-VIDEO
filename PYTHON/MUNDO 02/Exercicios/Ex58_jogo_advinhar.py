# Mundo 02: Exercício 58
"""
O computador vai "pensar" em um número de 0 e 10. Só que o jogador vai tentar adivinhar até acertar, mostrando no final
 quantos palpites foram necessários para vencer.
"""
import random
from time import sleep

computador = random.randint(0, 10)
print('-=-' * 20)
print('Vou pensar em um número entre 0 e 10. Tente advinhar...')
print('-=-' * 20)
jogador = int(input('Em que número eu pensei? '))
numero_jogadas = 1
while jogador != computador:
    print('PROCESSANDO...')
    sleep(1)
    if jogador < computador:
        print('VOCÊ PERDEU!!! Mais... Tente novamente.')
    else:
        print('VOCÊ PERDEU!!! Menos... Tente novamente.')
    jogador = int(input('Em que número eu pensei? '))
    numero_jogadas += 1
print('PROCESSANDO...')
sleep(1)
print('-=-' * 20)
print(' Você conseguiu me vencer!')
print(f' PARABÉNS! Eu pensei no número: {computador} e você precisou de {numero_jogadas} tentativas para acertar')
print('-=-' * 20)
print('FIM DO PROGRAMA')
