# Mundo 02: Exercício 36
"""
Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa. O programa vai perguntar o valor da
casa, o salário do comprador e em quantos anos ele vai pagar.

Calcule o valor da prestação mensal, sabendo que ela não pode exceder 30% do salário ou então o empréstimo será negado.
"""
casa = float(input('Qual o valor da casa? R$'))
salario = float(input('Qual o valor do salário do comprador? R$'))
anos = int(input('Em quantos anos de financiamento? '))
parcelas = anos * 12
prestacao = casa / (anos * 12)
if prestacao >= (salario * 0.30):
    print('Infelizmente seu empréstimo foi NEGADO')
else:
    print('Parabéns seu empréstimo foi APROVADO')
    print('Empréstimo parcelado em {} vezes de R${:.2f}\n'.format(parcelas, prestacao))
print('Simulação feita com sucesso!')