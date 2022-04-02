from time import sleep

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


def cadastrar(arq, nome='<desconhecido>', idade=0):
    try:
        a = open(arq, 'at')

    except Exception as erro:
        print('\033[31mErro ao tentar ler o arquivo!!\033[m')
        sleep(1)
        print(f'\033[31mPrograma finalizado por erro\033[m {erro.__class__}')

    else:
        try:
            a.write(f'{nome};{idade}\n')

        except Exception as erro:
            print('\033[31mErro ao tentar escrever no arquivo!!\033[m')
            sleep(1)
            print(f'\033[31mPrograma finalizado por erro\033[m {erro.__class__}')

        else:
            print(f'\033[33mNovo registro de\033[m \033[34:4m{nome}\033[m \033[33madicionado\033[m')
        finally:
            a.close()


