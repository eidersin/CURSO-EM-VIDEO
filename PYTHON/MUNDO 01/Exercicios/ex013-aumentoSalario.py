
# Exercício 13 – Reajuste Salarial

print('====== Exercício 13 – Reajuste Salarial')
salario = float(input('Qual o seu salário? R$'))
aumento = float(input('Qual a porcentagem de aumento? '))
soma = salario + (salario * aumento / 100)
aum = 1 + (aumento / 100)

print('O seu salário era R${:.2f} e com reajuste de {:.0f}% de aumento '
      'vai para {:.2f}'.format(salario, aumento, soma))

print('O seu salário era R${:.2f} e com reajuste de {:.0f}% '
      'de aumento vai para {:.2f}'.format(salario, aumento, salario*aum))
