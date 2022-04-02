print('======== DESAFIO 94 ========')
print('')

grupo = []
pessoa = {}
lista_mulh = []
lista_medi_idade = []

soma = 0
c = 1
while True:
    pessoa['Nome'] = str(input(f'Informe o nome da {c}ª pessoa: ')).strip()
    pessoa['Idade'] = int(input(f'Informe a idade da {c}ª pessoa: '))
    pessoa['Sexo'] = str(input(f'Informe o sexo da {c}ª pessoa: [M/F]')).upper().strip()[0]
    while pessoa['Sexo'] not in 'MF':
        pessoa['Sexo'] = str(input(f'ERRO!! Informe corretamente o sexo da {c}ª pessoa: [M/F]')).upper().strip()[0]

    grupo.append(pessoa.copy())
    pessoa.clear()

    print('-='*30+'|')
    esco = str(input('Quer continuar? [S/N]')).upper().strip()[0]
    while esco not in 'NS':
        esco = str(input('ERRO!! Digite corretamente, quer continuar? [S/N]')).upper().strip()[0]

    if esco == 'N':
        print('-='*30+'|')
        break

    print('-='*30+'|')
    c += 1

for pess in grupo:
    soma += pess['Idade']

    if pess['Sexo'] == 'F':
        lista_mulh.append(pess)

media_idade = soma / c

for pess in grupo:
    if pess['Idade'] > media_idade:
        lista_medi_idade.append(pess)

print(f'-A quantidade de pessoas cadastradas foi {c};')
print(f'-A média de idade do grupo foi de {media_idade:.2f} anos;')
print(f'-As mulheres cadastradas foram: ', end='')
for pess in lista_mulh:
    print(f'[\033[33m{pess["Nome"]}\033[m]', end=' ')

print(f'\n-As pessoas com idade acima da média foram:')
print('')
for pess in lista_medi_idade:
    print(f'    → \033[33mNOME:\033[m {pess["Nome"]} → \033[33mIDADE:\033[m {pess["Idade"]} → \033[33mSEXO:\033[m {pess["Sexo"]}')


