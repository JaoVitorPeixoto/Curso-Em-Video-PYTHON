print('======== DESAFIO 39 ========')
print('')

from datetime import date

nascimento = int(input('Informe o ano de nascimento: '))
ano_atual = date.today().year

idade = ano_atual - nascimento

if idade < 18:
    print(f'Você tem {idade} anos, vai se alistar em {ano_atual + (18 - idade)}.')

elif idade > 18:
    print(f'Você tem {idade} anos, já se alistou no ano de {ano_atual - (idade - 18)}.')

elif idade == 18:
    print(f'Você tem {idade}, já é hora de se alistar.')