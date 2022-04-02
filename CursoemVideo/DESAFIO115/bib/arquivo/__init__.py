from time import sleep


def arquivoExiste(arquivo):
    try:
        a = open(arquivo, 'rt')
        a.close()
    except FileNotFoundError:
        return False
    else:
        return True


def criarArquivo(nome):
    try:
        a = open(nome, mode='at')
        a.close()
    except Exception as erro:
        print('\033[31mErro ao tentar criar o arquivo!!\033[m')
        sleep(1)
        print(f'\033[31mPrograma finalizado por erro\033[m {erro.__class__}')
    else:
        print('\033[33mCriando arquivo...\033[m')
        sleep(1)
        print('\033[33mArquivo criado com sucesso!!\033[m')


def lerArquivo(arquivo):
    try:
        a = open(arquivo, 'rt')
    except Exception as erro:
        print('\033[31mErro ao tentar ler o arquivo!!\033[m')
        sleep(1)
        print(f'\033[31mPrograma finalizado por erro\033[m {erro.__class__}')
    else:
        for linha in a:
            dado = linha.split(';')
            dado[1] = dado[1].replace('\n', '')
            print(f'{dado[0]:<30} {dado[1]:>5} anos')
    finally:
        a.close()
