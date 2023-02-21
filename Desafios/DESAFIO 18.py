print('======== DESAFIO 18 ========')
print('')

from math import sin, cos, tan, radians

angulo = float(input('Informe o ângulo para achar o sen, cos e tg: '))

print('--'*20)
print(f'Com um ângulo de {angulo:.2f}°, temos que o sen é {sin(radians(angulo)):.2f}°, o cos é {cos(radians(angulo)):.2f}° e a tg é {tan(radians(angulo)):.2f}°')