print('======== DESAFIO 66 ========')
print('')

print('\033[37m-\033[m\033[35m=\033[m'*30)
cont = soma = 0
while True:
    num = int(input('Informe um número (digite 999 para parar): '))
    if num == 999:
        break
    cont += 1
    soma += num

print('\033[37m-\033[m\033[35m=\033[m'*30)
print(f'A quantidade de números digitados foi {cont}, e a soma deles é {soma}.')