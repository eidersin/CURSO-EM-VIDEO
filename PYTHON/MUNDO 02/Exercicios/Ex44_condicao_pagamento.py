# Mundo 02: Exercício 44
"""
Elabore um programa que calcule o valor a ser pago por um produto, considerando o seu preço normal e condição de
pagamento:
    - à vista dinheiro/cheque: 10% de desconto
    - à vista no cartão: 5% de desconto
    - em até 2x no cartão: preço normal
    - 3x ou mais no cartão: 20% de juros

"""
print(f'{" LOJAS DERSIN ":=^40}')
valor_produto = float(input('Qual o valor do produto: R$'))
print('1 - À vista\n'
      '2 - À vista no cartão\n'
      '3 - Dividir 2x no cartão\n'
      '4 - Dividir 3x ou mais no cartão')

forma_pagamento = int(input('Selecione a forma de pagamento: '))
if forma_pagamento == 1:
    valor1 = valor_produto - (valor_produto * 0.10)
    print(f'O valor a ser pago é: R${valor1:.2f} tendo 10% desconto.')

elif forma_pagamento == 2:
    valor2 = valor_produto - (valor_produto * 0.05)
    print(f'O valor a ser pago é: R${valor2:.2f} tendo 5% desconto.')

elif forma_pagamento == 3:
    valor3 = valor_produto / 2
    print(f'O valor a ser pago é: 2x de R${valor3:.2f} | Valor total: R${valor_produto:.2f}')

elif forma_pagamento == 4:
    numero_parcela = int(input('Deseja parcelar em quantas vezes? '))
    valor4 = valor_produto + (valor_produto * 0.2)
    parcelas = valor4 / numero_parcela
    print(f'O valor a ser pago é: {numero_parcela}x de R${parcelas:.2f} | Valor total: R${valor4:.2f}')
else:
    print('Forma de pagamento invalida')
