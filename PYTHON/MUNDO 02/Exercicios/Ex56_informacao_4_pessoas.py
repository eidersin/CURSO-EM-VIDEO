# Mundo 02: Exercício 56
"""
Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas. No final do programa, mostre:


"""
# Inicializa variáveis para armazenar a soma das idades e o nome do homem mais velho
soma_idades = 0
idade_homem_mais_velho = 0
nome_homem_mais_velho = ""
contagem_mulheres_menos_20 = 0

# Loop para coletar informações das 4 pessoas
for i in range(1, 5):
    print(f"Digite os dados da {i}º pessoa: ")
    nome = input("Nome: ")
    idade = int(input("Idade: "))
    sexo = input("Sexo (M/F): ").upper()

    # Soma as idades para calcular a média posteriormente
    soma_idades += idade

    # Verifica se é homem para comparar idade e atualizar os dados do homem mais velho
    if sexo == "M" and idade > idade_homem_mais_velho:
        idade_homem_mais_velho = idade
        nome_homem_mais_velho = nome

    # Conta as mulheres com menos de 20 anos
    if sexo == "F" and idade < 20:
        contagem_mulheres_menos_20 += 1

# Calcula a média de idade do grupo
media_idade = soma_idades / 4

# Exibe os resultados
print(f"\nA média de idade do grupo é: {media_idade:.2f} anos")
if nome_homem_mais_velho:
    print(f"O homem mais velho é: {nome_homem_mais_velho}, com {idade_homem_mais_velho} anos")
else:
    print("Não foi digitada informação de homem")
print(f"{contagem_mulheres_menos_20} mulher(es) têm menos de 20 anos")