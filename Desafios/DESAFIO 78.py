print('======== DESAFIO 78 ========')
print('')

valores = []

for c in range(0, 5):
    valores.append(int(input(f'Informe um valor para a posição {c}: ')))
print('-='*30)

print(f'Você digitou os valores: {valores}')
print(f'O maior valor é {max(valores)} e foi encontrado nas posições ', end='')
for c, v in enumerate(valores):
    if max(valores) == v:
        print(c, end='...')

print(f'\nO menor valor é {min(valores)} e foi encontrado nas posições ', end='')
for c, v in enumerate(valores):
    if min(valores) == v:
        print(c, end='...')

