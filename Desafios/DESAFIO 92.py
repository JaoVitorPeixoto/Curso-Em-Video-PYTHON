print('======== DESAFIO 92 ========')
print('')

from datetime import date

hoje = date.today().year

nome = str(input('Informe o nome da pessoa: ')).strip()
ano = int(input('Informe o ano de nascimento: '))
ctps = int(input('Informe o número da CTPS: [ 0 se não tiver ] '))

pessoa = {'Nome':nome , 'Idade': hoje-ano, 'CTPS': ctps }


if ctps != 0:
    pessoa['Contratado'] = int(input('Informe o ano de contratação do trabalho: '))
    pessoa['Salário'] = float(input('Agora informe o sálario: R$'))
    pessoa['Aposentadoria'] = pessoa['Idade'] + (35 - (hoje - pessoa['Contratado']))

print('-='*30)
print(pessoa)
for key, val in pessoa.items():
    print(f'{key}: {val}')





