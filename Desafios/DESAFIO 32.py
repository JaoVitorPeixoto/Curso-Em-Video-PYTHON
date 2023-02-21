print('======== DESAFIO 32 ========')
print('')

from datetime import date

ano = int(input('Informe um ano para saber se ele é um ano bissexto (informe <0> para saber do ano atual: '))
if ano == 0:
    ano = date.today().year

if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print(f'O ano {ano} é bissexto!!')

else:
    print(f'O ano {ano} não é bissexto!')