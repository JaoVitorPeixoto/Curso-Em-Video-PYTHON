print('======== DESAFIO 71 ========')
print('')

print('-='*20)
print('              BANCO 24H')
print('-='*20)

valor = int(input('Informe o valor a ser sacado: R$'))
print('--'*20)

c50 = c20 = c10 = c1 = 0
while True:
    if valor >= 50:
        valor -= 50
        c50 += 1

    elif 20 <= valor < 50:
        valor -= 20
        c20 += 1

    elif 10 <= valor < 20:
        valor -= 10
        c10 += 1

    elif 1 <= valor < 10:
        valor -= 1
        c1 += 1

    elif valor == 0:
        break

if c50 > 0:
    print(f'Total de \033[33m{c50}\033[m cédulas de \033[32mR$50\033[m')
if c20 > 0:
    print(f'Total de \033[33m{c20}\033[m cédulas de \033[32mR$20\033[m')
if c10 > 0:
    print(f'Total de \033[33m{c10}\033[m cédulas de \033[32mR$10\033[m')
if c1 > 0:
    print(f'Total de \033[33m{c1}\033[m cédulas de \033[32mR$1\033[m')

print('--'*20)
print('VOLTE SEMPRE AO BANCO CAIXA 24H!!!')