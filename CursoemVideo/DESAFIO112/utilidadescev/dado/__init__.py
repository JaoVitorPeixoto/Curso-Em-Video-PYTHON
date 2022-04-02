def leiaDinheiro(msg=''):
    num = str(input(f'{msg}')).strip()
    teste = num
    teste = teste.replace(',', '')
    teste = teste.replace('.', '')
    while True:
        if teste.isnumeric() and (num.count(',') + num.count('.')) < 2:
            break

        else:
            print(f'\033[31mERRO!! "{num.strip()}" é um preço inválido!!\033[m')
            num = str(input(f'{msg}')).strip()
            teste = num
            teste = teste.replace(',', '')
            teste = teste.replace('.', '')

    num = num.replace(',', '.')
    num = float(num)
    return num



