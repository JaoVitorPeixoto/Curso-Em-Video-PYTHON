def titulo(msg):
    print('\033[1m'+'-'*42)
    print(f'{msg.center(42)}')
    print('-'*42+'\033[m')


def menu(*lista, msg='MENU DE OPÇÕES'):
    """
    -> Função para criar um menu de acordo com o que o usuário desejar.
    :param lista: Uma lista com as opções na ordem desejada
    :param msg: (opcional) Qual o nome do menu de opções. OBS: O padrão é "MENU DE OPÇÕES"
    :return: sem retorno.
    """
    titulo(msg)
    cont = []
    for c in range(0, len(lista)):
        cont.append(c+1)
        print(f'\033[33m{c+1} -\033[m \033[34m{lista[c]}\033[m')

    print('\033[1m'+'-'*42, '\033[m')


    while True:
        try:
            esco = int(input('\033[33mESCOLHA:\033[m '))
        except:
            print('\033[31mERRO!! Informe corretamente!!\033[m')
        else:
            if esco in cont:
                break
            else:
                print('\033[31mERRO!! Informe corretamente!!\033[m')
    return esco


