
# Exercício 22 – Analisador de Textos

print('====== Exercício 22 – Analisador de Textos')

nome = input('Escreva seu nome completo: ').strip()
print('Seu nome em maiúsculas é {}'.format(nome.upper()))
print('Seu nome em maiúsculas é {}'.format(nome.lower()))
print('Seu nome tem ao todo {} letras'.format(len(nome) - nome.count(' ')))
print('Seu primeiro nome tem {} letras'.format(nome.find(' ')))
# ou
separa = nome.split()
print('Seu primeiro nome é {} e tem {} letras'.format(separa[0], len(separa[0])))