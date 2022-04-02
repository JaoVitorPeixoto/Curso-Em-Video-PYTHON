print('======== DESAFIO 38 ========')
print('')

print('====Informe 2 números inteiros para compará-los====')
print('')
num1 = int(input('Informe o primeiro número: '))
num2 = int(input('Informe o segundo número: '))
print('-='*20)

if num1 > num2:
    print('O \033[33mprimeiro valor\033[m é \033[34mmaior\033[m!!')

elif num1 < num2:
    print('O \033[33msegundo valor\033[m é \033[34mmaior\033[m!!')

elif num1 == num2:
    print('\033[33mNão existe\033[m valor maior, os dois são \033[34miguais\033[m!!')