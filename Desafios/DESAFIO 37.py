print('======== DESAFIO 37 ========')
print('')

num = int(input('Informe um número inteiro: '))

escolha = int(input('Agora escolha entre os números 1, 2 e 3 para converter em \033[31m<1>Binário\033[m, \033[32m<2>Octal\033[m e \033[34m<3>Hexadecimal\033[m: '))
print('-='*20)
if escolha == 1:
    print(f'O número \033[33m{num}\033[m em formato \033[31mbinário\033[m é \033[33m{bin(num)[2:]}\033[m.')
elif escolha == 2:
    print(f'O número \033[33m{num}\033[m em formato \033[32moctal\033[m é \033[33m{oct(num)[2:]}\033[m.')
elif escolha == 3:
    print(f'O número \033[33m{num}\033[m em formato \033[34mhexadecimal\033[m é \033[33m{hex(num)[2:]}\033[m.')
else:
    print('\033[31mERRO!!! Tente novamente')