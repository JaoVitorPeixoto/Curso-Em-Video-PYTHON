print('')
print('===INFORME 4 NÚMEROS PARA A SOMA===')
print('')

soma = 0
for c in range(0, 4):
    n = int(input(f'Informe o {c+1}° número: '))
    soma = soma + n

print('-='*20)
print(f'O reulstado final é {soma}.')
print('-='*20)