print('======== DESAFIO 11 ========')
print('')

base = float(input('Informe a largura(ou base) da parede: '))
altura = float(input('Informe o comprimento(ou altura) da parede: '))
area = base * altura
qntd = area / 2 #quantidade pintada usando 1 litro de tinda dada no desafio.
print('A área é: {}m²'.format(area))
print('A quantidade de tinta usada será: {}L'.format(qntd))
