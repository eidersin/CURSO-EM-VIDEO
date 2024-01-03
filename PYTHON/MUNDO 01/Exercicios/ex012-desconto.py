
# Exercício 12 – Calculando Descontos

print('====== Exercício 12 – Calculando Descontos')
valor = eval(input('Qual o valor do produto? R$'))
# des5 = 1-0.05
des5 = valor - (valor * 5 / 100)
print('O produto que custava R${} com 5% de desconto vai custar R${:.2f}'.format(valor, des5))
