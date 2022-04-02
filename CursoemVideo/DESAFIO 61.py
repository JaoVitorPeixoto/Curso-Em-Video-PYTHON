print('======== DESAFIO 61 ========')
print('')

primeiro = int(input('Informe o primeiro termo da PA: '))
razão = int(input('Agora informe a razão dessa PA: '))
print('-='*20)

print('Os 10 primeiros termos dessa PA são:')
c = 0
print('(', end='')
while c < 10:
    print(f'{primeiro}', end=', 'if c!=9 else '...)')
    primeiro += razão
    c += 1

print('\n'+'-='*20)
