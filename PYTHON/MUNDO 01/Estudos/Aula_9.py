frase = 'Curso em Video Python'
frase2 = '  Aprenda Python  '

# Fatiamento
print(frase[9])
print(frase[9:14])
print(frase[9:21])
print(frase[9:21:2])    #Começa no 9 e vai até 21 pulando de 2 em 2
print(frase[:5])
print(frase[15:])
print(frase[9::3])      #Começa no 9 e vai até o final pulando de 3 em 3

# Análise
print(len(frase))                               # len = Comprimento da frase
print(frase.count('o'))                         # count = Conta quantos vezes existe o 'valor'
print(frase.count('o', 0, 13))   # count = Conta quantos vezes existe o 'valor' (entre 0 e 13)
print(frase.find('deo'))                        # find = Fala em que posição começou o 'valor' procurado
print(frase.find('android'))                    # find = Se o resultado foi -1 ele não encontrou o 'valor' na frase.
print('Curso' in frase)                       # 'valor' in variavel = Ele tras True or False se existe o valor na frase

# Transformação
print(frase.replace('Python', 'Android')) # replace = Substitui '_old: valor' para '_new: valor'
print(frase.upper())            # upper = Ficar em letra maiúscula
print(frase.lower())            # lower = Fica em letra minúscula
print(frase.capitalize())       # capitalize = Pega a string coloca em minúscula e coloca a primeira letra em maiúscula
print(frase.title())            # title =  Transforma toda string após espaço em Maiúscula


print(frase2.strip())            # strip = Remove espaços inúteis na frase.
print(frase2.rstrip())           # strip = Remove espaços inúteis da direita na frase.
print(frase2.lstrip())           # strip = Remove espaços inúteis da esquerda na frase.

# Divisão
print(frase.split())            # split = Gera uma lista com todas as palavras de uma cadeia de caracteres
# Junção
print(''.join(frase))

# TESTES

