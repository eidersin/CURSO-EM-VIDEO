largura = eval(input('Qual a largura da parede em metros? '))
alt = eval(input('Qual a altura da parede em metros? '))
area = largura * alt
tinta = area / 2
print('Sua parede tem a area de {}m2 e vai precisar de {} litros de tinta'.format(area, tinta))
