# CONDIÇÕES ANINHADAS
"""
if  #Inicializado a classe
    BLOCO 01
elif # Pode utilizar quantos quiser.
    BLOCO 02
else: # Pode utilizar uma ou nenhuma vez.
    BLOCO 03

Exemplo:

    nome = str(input('Qual é seu nome? ')).capitalize().strip()
    if nome == 'Wanderson':
        print('Que nome bonito!')
    elif nome == 'Pedro' or nome == 'Maria' or nome == 'João':
        print('Seu nome é bem popular no Brasil')
    elif nome in 'Fernanda Ana Claudia Jéssica Juliana':
        print('Belo nome feminino')
    else:
        print('Seu nome é bem normal.')
    print('Tenha um bom dia, {}!'.format(nome))

"""