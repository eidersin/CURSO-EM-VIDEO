# Mundo 02: Exercício 53
"""
Faça um programa que leia um número inteiro e diga se ele é ou não um número primo
"""
num = eval(input('Digite um número: '))
total = 0
for c in range(1, num + 1):
    if num % c == 0:
        total += 1
print('O número {} foi divisivel {} vezes'.format(num, total))
if total == 2:
    print('Então o número é PRIMO')
else:
    print('Então o número NÃO é PRIMO')



""" 
# CALCULO PRIMO (Chat GPT)
def eh_primo(n):
    if n < 2:
        return False
    i = n // 2
    while i > 1:
        if n % i == 0:
            return False
        i -= 1
    return True
def imprimir_resultado(numero, resultado):
    mensagem = f'O número {numero} NÃO é primo'
    if (resultado):
        mensagem = f'O número {numero} é primo'
    return mensagem

numero = eval(input('Digite um numero: '))
resultado = eh_primo(numero)
msg = imprimir_resultado(numero, resultado)
print(msg)
"""