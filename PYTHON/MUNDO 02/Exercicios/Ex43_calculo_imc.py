# Mundo 02: Exercício 43
"""
Desenvolva uma lógica que leia o peso e a altura de uma pessoa, calcule seu IMC e mostre seu status de acordo com a
tabela abaixo:
    - Abaixo de 18.5: Abaixo do Peso
    - Entre 18.5 e 25: Peso Ideal
    - 25 até 30: Sobrepeso
    - 30 até 40: Obesidade
    - Acima de 40: Obesidade Morbida

"""

peso = float(input('Qual o seu peso? (Kg) '))
altura = float(input('Qual sua altura? (m) '))
imc = peso / (altura ** 2)
if imc < 18.5:
    print(f'O seu IMC é {imc:.1f} e você esta abaixo do peso')
elif imc <= 25:
    print(f'O seu IMC é {imc:.1f} e você esta no peso ideal')
elif imc <= 30:
    print(f'O seu IMC é {imc:.1f} e você esta com sobrepeso')
elif imc <= 40:
    print(f'O seu IMC é {imc:.1f} e você esta com obesidade')
else:
    print(f'O seu IMC é {imc:.1f} e você esta com obsedidade mórbida! Procure um Médico')
