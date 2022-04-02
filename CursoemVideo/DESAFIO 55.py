print('======== DESAFIO 55 ========')
print('')

menor = 0
maior = 0
for c in range(0, 5):
    peso = float(input(f'Informe o peso da {c+1}ª pessoa: '))

    if c == 0:
        maior = peso
        menor = peso

    else:
        if peso > maior:
            maior = peso

        elif peso == maior:
            maior = peso

        elif peso == menor:
            menor = peso

        else:
            menor = peso

print(f'O maior peso foi {maior}, e o menor peso foi {menor}')
