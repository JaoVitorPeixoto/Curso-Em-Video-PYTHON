print('======== DESAFIO 75 ========')
print('')


numeros = (int(input('Informe um número: ')),
           int(input('Informe outro número: ')),
           int(input('Informe mais um número: ')),
           int(input('Informe o ultimo número: ')))

print('-='*30)

print(f'Você digitou os valores {numeros}')
print(f'O valor 9 apareceu {numeros.count(9)} vezes na tupla;')
print('O valor 3 não foi digitado em nenhuma posição;' if(3 not in numeros) else f'O valor 3 foi digitado na {(numeros.index(3))+1}ª posição;')
print('Os valores pares digitados foram:', end=' ')

for c in numeros:
    if c % 2 == 0:
        print(c, end=' ')

print('')
