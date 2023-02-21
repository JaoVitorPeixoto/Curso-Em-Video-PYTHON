print('======== DESAFIO 85 ========')
print('')

pares = []
impares = []
numeros = [pares, impares]

for c in range(1, 8):
    núm = int(input(f'Informe o {c}º número: '))

    if núm % 2 == 0:
       pares.append(núm)
    else:
        impares.append(núm)

print('-='*30)
pares.sort()
impares.sort()
numeros.sort()
print(f'Os números são: {numeros}')
print(f'Os números pares são: {pares}')
print(f'Os números ímpares são: {impares}')