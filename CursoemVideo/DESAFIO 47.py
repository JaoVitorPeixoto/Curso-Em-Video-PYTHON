print('======== DESAFIO 47 ========')
print('')

print('Informe o intervalo para saber todos os números pares ou ímpares nele.')

i = int(input('\033[4;33mINÍCIO\033[m do intervalo: '))
f = int(input('\033[4;33mFIM\033[m do intervalo: '))
print('-='*20)

print('Agora informe \033[31m[ 0 ]\033[m para ver todos números ímpares ou \033[34m[ 1 ]\033[m para números pares.')
escolha = int(input('ESCOLHA: '))
print('-='*20)

if escolha == 0:
    for c in range(i, f+1):
        if c % 2 == 1:
            print(c, end=' ')

elif escolha == 1:
    for c in range(i, f+1):
        if c % 2 == 0:
            print(c, end=' ')

else:
    print('\033[1;31mERRO!! TENTE NOVAMENTE!!\033[m')

print('')
print('\nFIM!!')