# Exercício extra: 01
"""
Crie um programa que leia dois valores e mostre um menu na tela:
"""
continuar_programa = ()
while continuar_programa != 0:
    print('[1] Somar\n'
          '[2] Subtrair\n'
          '[3] Multiplicar\n'
          '[0] Para sair')
    escolha_operador = int(input('Deseja utilizar qual operador?: '))
    if escolha_operador == 1:
        continuar_operador = 'S'
        while continuar_operador.upper() == 'S':
            print('Você escolheu o operador: Somar')
            n1 = int(input('Digite o primeiro valor: '))
            n2 = int(input('Digite o segundo valor: '))
            soma = n1 + n2
            print('{} + {} vale: {}'.format(n1, n2, soma))
            continuar_operador = str(input('Deseja continuar? [S/N]')).upper().strip()
    elif escolha_operador == 2:
        continuar_operador = 'S'
        while continuar_operador.upper() == 'S':
            print('Você escolheu o operador: Subtrair')
            n1 = int(input('Digite o primeiro valor: '))
            n2 = int(input('Digite o segundo valor: '))
            soma = n1 - n2
            print('{} - {} vale: {}'.format(n1, n2, soma))
            continuar_operador = str(input('Deseja continuar? [S/N]')).upper().strip()
    elif escolha_operador == 3:
        continuar_operador = 'S'
        while continuar_operador.upper() == 'S':
            print('Você escolheu o operador: Multiplicar')
            n1 = int(input('Digite o primeiro valor: '))
            n2 = int(input('Digite o segundo valor: '))
            soma = n1 * n2
            print('{} x {} vale: {}'.format(n1, n2, soma))
            continuar_operador = str(input('Deseja continuar? [S/N]')).upper().strip()
    elif escolha_operador == 0:
        break
    else:
        print('Escolha de operador inválida. Tente novamente.')
print('Fim do programa')
