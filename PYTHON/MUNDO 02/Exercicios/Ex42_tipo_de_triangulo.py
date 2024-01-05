# Mundo 02: Exercício 42
"""
Refaça o DESAFIO 035 dos triângulos, acrescentando o recurso de mostrar que tipo de triângulo será formado:
 - Equilatero: todos os lados iguais
 - Isosceles: dois lados iguais
 - Escaleno: todos os lados diferentes

"""
a = float(input('Digite o valor da primeira reta: '))
b = float(input('Digite o valor da segunda reta: '))
c = float(input('Digite o valor da terceira reta: '))
if a < b + c and b < a + c and c < a + b:
    print('Os segmentos acima PODEM FORMAR um triangulo')
    if a == b == c:
        print('O triangulo tem todos os lados iguais! É do tipo Equilátero')
    elif a == b or a == c or b == c:
        print('O triangulo tem dois lados iguais! É do tipo Isóceles')
    elif a != b and a != c and b != c:
        print('O triangulo tem todos os lados diferentes! É do tipo Escaleno')
else:
    print('Os segmentos acima NÃO PODEM FORMAR um triangulo')
