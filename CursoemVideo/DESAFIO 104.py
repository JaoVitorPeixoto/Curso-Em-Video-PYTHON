def leiaint(frase=''):
    n = str(input(f'{frase}'))
    while n.isnumeric() == False:
        print('\033[31mERRO!! Informe um número inteiro!!\033[m')
        n = str(input(f'{frase}'))
    n = int(n)
    return n


# Programa principal >>>>>>>>
print('======== DESAFIO 104 ========')
print('')

n = leiaint('Me informa um número ae: ')
print(f'O número informado foi {n}')