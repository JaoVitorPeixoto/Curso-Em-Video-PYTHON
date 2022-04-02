print('======== DESAFIO 40 ========')
print('')

n1 = float(input('Informe a nota 1 do aluno: '))
n2 = float(input('Informe a nota 2 do aluno: '))

media = (n1 + n2) / 2

if media >= 7:
    print(f'Sua média foi de \033[36m{media:.2f}\033[m, então você está \033[4;32maprovado\033[m!!!')

elif (media >= 5) and (media < 7):
    print(f'Sua média foi de \033[36m{media:.2f}\033[m, então você ficou na \033[4;33mrecuperação\033[m!!')

elif media < 5:
    print(f'Sua média foi de \033[36m{media:.2f}\033[m, então você foi \033[4;31mreprovado\033[m!!!')