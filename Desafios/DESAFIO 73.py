print('======== DESAFIO 73 ========')
print('')

brasileirão = ('Atlético-MG', 'Flamengo', 'Palmeiras', 'Fortaleza', 'Corinthians',
               'Bragantino', 'Fluminense', 'América-MG', 'Atlético-GO', 'Santos',
               'Ceará SC', 'Internacional', 'São Paulo', 'Athletico-PR', 'Cuiabá',
               'Juventude', 'Grêmio', 'Bahia', 'Sport Recife', 'Chapecoense')

print(f'Os times do brasileirão: \033[33m{brasileirão}\033[m')
print('-='*150)
print(f'Os times em ordem alfabética: \033[33m{sorted(brasileirão)}\033[m')
print('-='*150)
print(f'Os 5 primeiros colocados: \033[32m{brasileirão[:5]}\033[m')
print('-='*80)
print(f'Os 4 últimos colocados: \033[31m{brasileirão[16:]}\033[m')
print('-='*80)

proc = str(input('Informe o time que quer procurar na tupla: ')).strip()
while proc not in brasileirão:
    proc = str(input('ERRO!! Informe o nome do time corretamente: ')).strip()

print(f'O time \033[33m{brasileirão[brasileirão.index(proc)]}\033[m está na \033[33m{(brasileirão.index(proc))+1}ª\033[m posição.')
