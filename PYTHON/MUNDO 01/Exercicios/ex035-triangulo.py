a = float(input('Digite o valor da primeira reta: '))
b = float(input('Digite o valor da segunda reta: '))
c = float(input('Digite o valor da terceira reta: '))
if a < b + c and b < a + c and c < a + b:
    print('Os segmentos acima PODEM FORMAR um triangulo')
else:
    print('Os segmentos acima NÃO PODEM FORMAR um triangulo')
