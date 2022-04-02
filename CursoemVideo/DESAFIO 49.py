print('======== DESAFIO 49 ========')
print('')

n = int(input('Informe o número para a tabuada: '))
print('-='*20)

for c in range(1, 11):
    print(f' | \033[1m{n:<2}\033[m x {c:2} = \033[32m{n*c:2}\033[m | ' )
print('-='*20)