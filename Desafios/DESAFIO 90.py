print('======== DESAFIO 90 ========')
print('')

aluno = {}

aluno['Nome'] = str(input('Informe o nome do aluno: ')).strip()
aluno['Média'] = float(input('Informe a média do aluno: '))

if aluno['Média'] >= 6:
    aluno['Situação'] = '\033[32mAPROVADO\033[m'

elif aluno['Média'] < 4.5:
    aluno['Situação'] = '\033[31mREPROVADO\033[m'

else:
    aluno['Situação'] = '\033[33mRECUPERAÇÃO\033[m'

print('-='*30)
for key, val in aluno.items():
    print(f'    {key}: {val:}')