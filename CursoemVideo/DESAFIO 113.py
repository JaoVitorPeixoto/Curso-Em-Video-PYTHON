def leiaInt(msg):
    while True:
        try:
            num = int(input(msg))
        except KeyboardInterrupt:
            print('\033[31m\nO usuário decidiu não informar o número, então ele será 0.\033[m')
            return 0
        except:
            print(f'\033[31mERRO!! Informe um número inteiro válido!\033[m')
        else:
            return num
            break


def leiaFloat(msg):
    while True:
        try:
            num = float(input(msg))
        except KeyboardInterrupt:
            print('\033[31m\nO usuário decidiu não informar o número, então ele será 0.\033[m')
            return 0
        except:
            print(f'\033[31mERRO!! Informe um número float válido!\033[m')
        else:
            return num
            break




# Programa principal >>>>>>
print('======== DESAFIO 113 ========')
print('')

n1 = leiaInt('Informe um número inteiro: ')
n2 = leiaFloat('Informe um número Real: ')
print('--'*30)
print(f'O número inteiro informado foi {n1}')
print(f'O número Real informado foi {n2}')