print('======== DESAFIO 69 ========')
print('')

from time import sleep

maioridade = masculino = mulhermenor = 0
c = 1
while True:
    sexo = str(input(f'Informe o sexo da {c}ª pessoa [M/F]: ')).upper().strip()[0]
    while sexo not in 'MF':
        sexo = str(input(f'Erro!! informe o sexo corretamente [M/F]: ')).upper().strip()[0]

    idade = int(input(f'Informe a idade da {c}ª pessoa: '))
    print('--' * 30)

    if idade >= 18:
        maioridade += 1

    if sexo == 'M':
        masculino += 1

    if sexo == 'F' and idade <= 20:
        mulhermenor += 1

    escolha = str(input('Quer cadastrar mais uma pessoa? [S/N] ')).upper().strip()[0]
    while escolha not in 'SN':
        escolha = str(input('Erro!! informe corretamente: [S/N] ')).upper().strip()[0]

    if escolha == 'N':
        print('Ok finalizando...')
        print('-='*30)
        sleep(1)
        break

    c += 1

print(f'''A quantidade de mulheres com idade menor que 20 anos é \033[33m{mulhermenor}\033[m;
Existem \033[33m{maioridade}\033[m pessoas com mais de 18 anos;
Foram cadastrados \033[33m{masculino}\033[m homens.''')