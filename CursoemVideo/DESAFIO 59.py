print('======== DESAFIO 58 ========')
print('')

num1 = float(input('Informe o primeiro número: '))
num2 = float(input('Informe o segundo número: '))
escolha = 0
print('-='*20)
while escolha != 5:


    print('''Você quer...
\033[33m[ 1 ]\033[m \033[34mSOMAR\033[m
\033[33m[ 2 ]\033[m \033[34mMULTIPLICAR\033[m
\033[33m[ 3 ]\033[m \033[34mQUAL O MAIOR\033[m
\033[33m[ 4 ]\033[m \033[34mESCOLHER NOVOS NÚMEROS\033[m
\033[33m[ 5 ]\033[m \033[34mSAIR\033[m''')

    escolha = int(input('Escolha: '))
    print('-='*20)
    while escolha != 1 and escolha != 2 and escolha !=3 and escolha != 4 and escolha != 5:
        escolha = int(input('\033[31mNúmero informado é invalido\033[m, informe novamente!!: '))

    if escolha == 1:
        print(f'A \033[34mSOMA\033[m dos números \033[33m{num1}\033[m e \033[33m{num2}\033[m é igual a \033[34m{num1+num2}\033[m')
        print('-='*20)

    elif escolha == 2:
        print(f'A \033[34mMULTIPLICAÇÃO\033[m dos números \033[33m{num1}\033[m e \033[33m{num2}\033[m é igual a \033[34m{num1*num2}\033[m')
        print('-=' * 20)

    elif escolha == 3:
        if num1 > num2:
            print(f'O número \033[33m{num1}\033[m é \033[34mMAIOR\033[m que \033[33m{num2}\033[m')

        elif num1 == num2:
            print(f'O número \033[33m{num1}\033[m é \033[34mIGUAL\033[m a \033[33m{num2}\033[m')

        else:
            print(f'O número \033[33m{num2}\033[m é \033[34mMAIOR\033[m que \033[33m{num1}\033[m')
        print('-=' * 20)

    elif escolha == 4:
        num1 = float(input('Informe o \033[34mNOVO\033[m \033[33m"primeiro número"\033[m: '))
        num2 = float(input('Informe o \033[34mNOVO\033[m \033[33m"segundo número"\033[m: '))
        print('-='*20)

print('\033[32mPrograma encerrado...\033[m')