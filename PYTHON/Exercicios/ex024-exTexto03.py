# Crie um programa que leaia o nome de uma cidade e diga se ela começa ou não com "SANTO".

# Exercício 24 – Verificando as primeiras letras de um texto

print('====== Exercício 24 – Verificando as primeiras letras de um texto')
cidade = str(input('Qual nome da sua cidade? ')).strip(' ').capitalize()
separar = cidade.split()
teste = ('Santo' in (separar[0]))
print('O nome da cidade de {} começa com a palavra SANTO? {} '.format(cidade, teste))