print('======== DESAFIO 52 ========')
print('')

num = int(input('Informe um número para saber se ele é um número primo ou não: '))
print('-='*50)

i = 0
for c in range(1, num+1):
    if num % c == 0:
        print(f'\033[32m{c}\033[m', end=' ')
        i = i + 1
    else:
        print(f'\033[31m{c}\033[m', end=' ')

print('\n', '-='*50)
print(f'O número \033[33m{num}\033[m é divisível \033[33m{i}\033[m vezes,', f'por 1 e por \033[33m{num}\033[m, então \033[4;32mELE É\033[m um número primo' if i==2  else f'então ele \033[4;31mNÃO È\033[m um número primo.')