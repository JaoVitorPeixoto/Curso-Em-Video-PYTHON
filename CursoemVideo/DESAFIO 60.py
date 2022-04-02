print('======== DESAFIO 60 ========')
print('')

num = int(input('Informe um número para saber seu fatorial: '))
print('\033[35m-\033[37m=\033[m'*20)

c = num
while c > 0:
    print(f'\033[33m{c}\033[m', end=' x ' if c!=1 else ' = ')
    if c != num:
        num = c*num
    c -= 1

print(f'\033[36m{num}\033[m')
print('\033[35m-\033[37m=\033[m'*20)