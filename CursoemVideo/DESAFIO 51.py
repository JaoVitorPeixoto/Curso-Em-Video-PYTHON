print('======== DESAFIO 51 ========')
print('')

r = int(input('Informe a razão dessa PA: '))
pt = int(input('Agora informe o primeiro termo dessa PA: '))
print('')
print('Os 10 primeiros termos dessa PA são:')
print('-='*20)

dc = pt + (10 - 1) * r
print('(', end='')
for c in range(pt, dc + 1, r):
    print(f'{c}...)'if c==dc else f'{c}, ' , end='')


print('\n'+'-='*20)