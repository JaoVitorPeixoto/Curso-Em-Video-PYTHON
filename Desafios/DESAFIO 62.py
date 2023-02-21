print('======== DESAFIO 62 ========')
print('')

primeiro = int(input('Informe o primeiro termo da PA: '))
razão = int(input('Agora informe a razão dessa PA: '))
print('-='*30)

print('Os 10 primeiros termos dessa PA são:')
c = 0
termos = 10
print('(', end='')
while c < termos:
    print(f'\033[33m{primeiro}\033[m', end=', 'if c!=termos-1 else '...)')
    primeiro += razão
    c += 1
    if c == termos:
        print('\n'+'-='*30)
        c = 0
        termos = int(input('Você quer mostrar mais quantos termos? digite [ 0 ] para parar: '))
        print('-='*30)
        print(end='(...'if termos!=0 else '')


