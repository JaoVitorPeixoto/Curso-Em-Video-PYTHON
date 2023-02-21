print('======== DESAFIO 17 ========')
print('')

from math import hypot

cato = float(input('Informe o comprimento do cateto oposto: '))
cata = float(input('Agora informe o comprimento do cateto adjacente: '))

print('-'*20)
print(f'O cateto oposto é {cato:.2f} e o adjacente é {cata:.2f}, então a hipotenusa é igual a {hypot(cato, cata):.2f}')