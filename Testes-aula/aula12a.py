nome = str(input('Informe seu nome: '))

if nome.upper() in 'JOÃO VITOR' :
    print (f'\033[4;34m{nome}\033[m... \033[32mQue nome bonito!!\033[m')

elif 'WESLEY' in nome.upper() :
    print(f'\033[4;34m{nome}\033[m... \033[31mQue nome feio!!!\033[m')

else:
    print('Seu nome é bem normal...')
print(f'Tenha um bom dia, {nome}!!')