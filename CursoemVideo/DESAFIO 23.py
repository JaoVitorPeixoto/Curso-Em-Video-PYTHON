print('======== DESAFIO 23 ========')
print('')

num = int(input('Informe um número inteiro de 0 a 9999: '))

u = num // 1 % 10
d = num // 10 % 10
c = num // 100 % 10
m = num // 1000 % 10

print(f'Unidade: {u:>4}')
print(f'Dezena: {d:>5}')
print(f'Centena:{c:>5}')
print(f'Milhar: {m:>5}')