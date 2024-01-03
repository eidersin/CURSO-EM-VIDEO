salario = float(input('Qual o seu salario? R$'))
if salario > 1250:
    aum = salario * 10 / 100
    novoSalario = salario + aum
else:
    aum = salario * 15 / 100
    novoSalario = salario + aum

print('Seu aumento é de {} e seu novo salário é {}'.format(aum, novoSalario))