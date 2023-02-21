print('======== DESAFIO 56 ========')
print('')

media = 0
maior = 0
contadorm = 0
for c in range (0, 4):
    nome = str(input(f'Informe o nome da {c+1}ª pessoa: ')).strip()
    idade = int(input(f'Informe a idade da {c+1}ª pessoa: '))
    sexo = str(input(f'Informe o sexo da {c+1}ª pessoa [ Homem ] ou [ Mulher ]: ')).strip()
    print('-='*20)

    if sexo.upper() == 'HOMEM' and idade > maior:
        maior = idade
        homemvelho = nome

    if sexo.upper() == 'MULHER' and idade <= 20:
        contadorm = contadorm + 1
    media = media + idade

print(f'O a média de idade desse grupo de pessoas é {media/4:.2f};')
print(f'{homemvelho} tem {maior} anos, e é o homem mais velho desse grupo;')
print(f'Nesse grupo existe(em) {contadorm} mulher(es) com idade menor que 20 anos.')