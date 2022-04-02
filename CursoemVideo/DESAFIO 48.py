print('======== DESAFIO 48 ========')
print('')
soma = 0
for c in range(1, 501, 2):
    if c % 3 == 0:
        soma = soma + c

print(f'A soma de todos os números imparis multiplos de 3 nesse intervalo é {soma}.')