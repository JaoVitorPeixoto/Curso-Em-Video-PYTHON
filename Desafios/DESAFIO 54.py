print('======== DESAFIO 54 ========')
print('')

from datetime import date

cmenor = 0
cmaior = 0
for c in range(0, 7):
    ano = int(input(f'Informe o ano de nacsimento da {c+1}° pessoa: '))
    idade = date.today().year - ano

    if idade < 18:
        cmenor = cmenor + 1

    else:
        cmaior = cmaior + 1

print('-='*20)
print(f'A quantidade de pessoas menores de idade é de {cmenor} pessoas, e maiores de idade é de {cmaior} pessoas.')