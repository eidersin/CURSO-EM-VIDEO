
# Exercício 10 – Conversor de Moedas

print('====== Exercício 10 – Conversor de Moedas')
num = eval(input('Qual quantidade de dinheiro voce tem na carteira? R$'))
print('Com R${} você pode comprar US${:.2f}'.format(num, num/3.27))