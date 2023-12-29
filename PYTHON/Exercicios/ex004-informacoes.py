
# Exercício 4 – Dissecando uma Variável

print('====== Exercício 4 – Dissecando uma Variável')
valor = input('Digite o primeiro valor: ')
print(f'O valor é um número: {valor.isnumeric()}')
print(f'O valor é um espaço: {valor.isspace()}')
print(f'O valor é um Alphanumerico: {valor.isalnum()}')
print(f'O valor é maiusculo: {valor.isupper()}')
print(f'O valor é uma letra: {valor.isalpha()}')
print(f'O valor é um Decimal: {valor.isdecimal()}')
