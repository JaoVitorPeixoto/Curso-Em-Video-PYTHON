print('======== DESAFIO 80 ========')
print('')

valores = []


for c in range(0, 5):
    v = int(input('Informe um número: '))

    if c == 0 or v > valores[-1]:
        print(f'{v} adicionado no final da lista...')
        valores.append(v)

    else:
        posição = 0
        while posição < len(valores):
            if v <= valores[posição]:
                print(f'{v} adicionado na posição {posição} da lista...')
                valores.insert(posição, v)
                break

            posição += 1

    print('-='*30)

print(f'A lista em ordem é {valores}')



