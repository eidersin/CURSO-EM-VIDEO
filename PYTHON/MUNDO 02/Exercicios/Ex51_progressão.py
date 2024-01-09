# Mundo 02: Exercício 51
"""
Desenvolva um programa que leia o primeiro termo e a razão de uma PA. No final, mostre os 10 primeiros termos dessa
progressão.
"""


# Função para gerar os termos da PA
def gerar_pa(primeiro_termo, razao, quantidade):
    termos = [primeiro_termo + i * razao for i in range(quantidade)]
    return termos


# Função principal
def main():
    # Solicita ao usuário o primeiro termo e a razão da PA
    primeiro_termo = float(input("Digite o primeiro termo da PA: "))
    razao = float(input("Digite a razão da PA: "))

    # Define a quantidade de termos a serem exibidos (neste caso, 10)
    quantidade_termos = 10

    # Gera os termos da PA chamando a função gerar_pa
    termos_pa = gerar_pa(primeiro_termo, razao, quantidade_termos)

    # Exibe os termos gerados
    print(f"\nOs {quantidade_termos} primeiros termos da PA são:")
    for termo in termos_pa:
        print('{}'.format(termo))


# Chama a função principal
if __name__ == "__main__":
    main()