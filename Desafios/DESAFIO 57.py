print('======== DESAFIO 57 ========')
print('')

sex = str(input('Informe [M/F] para homem(M) ou mulher(F): ')).strip().upper()[0]
print('-='*20)

while sex not in 'MF':
    sex = str(input('ERRO!! Informe corretamente [M/F]: ')).strip().upper()[0]

print('')
print(f'Ok!! então vc é {"Masculino"if sex == "M" else "Feminino"}')