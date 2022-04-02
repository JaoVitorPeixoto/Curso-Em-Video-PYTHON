print('======== DESAFIO 50 ========')
print('')

soma = 0

for c in range(1, 7):
    n = int(input(f'Informe o \033[33m{c}°\033[m número para a soma: '))
    if n % 2 == 0:
        soma = soma + n

print('-='*20)
print(f'O resultado da soma dos números pares é \033[34m{soma}\033[m')