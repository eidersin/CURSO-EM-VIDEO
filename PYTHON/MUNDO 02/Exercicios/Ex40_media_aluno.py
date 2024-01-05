# Mundo 02: Exercício 40
"""
Crie um programa que leia duas notas de um aluno e calcule sua média, mostrando uma mensagem no final, de acordo
com a média atingida:
    - Média abaixo de 5.0: REPROVADO
    - Média entre 5.0 e 6.9: RECUPERAÇÃO
    - Média 7.0 ou superior: APROVADO
"""
nota1 = float(input('Qual o valor da primeira nota? '))
nota2 = float(input('Qual o valor da segunda nota? '))
media = (nota1 + nota2) / 2
print('Tirando {} e {}, a média do aluno é {:.1f}'.format(nota1, nota2, media))
if media < 5:
    print('O Aluno foi REPROVADO')
elif media <= 6.9:
    print('O aluno esta de RECUPERAÇÃO')
else:
    print('O Aluno foi APROVADO')
