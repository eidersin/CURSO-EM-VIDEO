a = int(input('Digite primeiro número: '))
b = int(input('Digite segundo número: '))
c = int(input('Digite terceiro número: '))
# MEU CÓDIGO
# if num1 > num2 > num3:
#     maior = num1
#     menor = num3
# elif num1 > num3 > num2:
#     maior = num1
#     menor = num2
#
# elif num2 > num1 > num3:
#     maior = num2
#     menor = num3
# elif num2 > num3 > num1:
#     maior = num2
#     menor = num1
#
# elif num3 > num2 > num1:
#     maior = num3
#     menor = num2
# elif num3 > num1 > num2:
#     maior = num3
#     menor = num1
# else:
#     print('Número invalido')

# CÓDIGO APRENDIDO:
# VERIFICANDO O MENOR VALOR
menor = a
if b < a and b < c:
    menor = b
if c < a and c < b:
    menor = c
# VERIFICANDO O MAIOR VALOR
maior = a
if b > a and b > c:
    maior = b
if c > a and c > b:
    maior = c
print('O menor valor digitado foi {}'.format(menor))
print('O maior valor digitado foi {}'.format(maior))
