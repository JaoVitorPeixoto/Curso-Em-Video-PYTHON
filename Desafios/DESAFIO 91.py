
from random import randint
from time import sleep
from operator import itemgetter

print('-='*30)
print(f'{"JOGANDO DADOS":^60}')
print('-='*30)
sleep(1)

ranking = {}
jogadores = {'Jogador-1': randint(1, 6),
             'Jogador-2': randint(1, 6),
             'Jogador-3': randint(1, 6),
             'Jogador-4': randint(1, 6)}

print(' Tabela de valores sorteados:')
sleep(1)
for key, val in jogadores.items():
    print(f'     O \033[33m{key}\033[m tirou \033[34m{val}\033[m')
    sleep(1)

ranking = sorted(jogadores.items(), key=itemgetter(1), reverse=True)

print('--'*30)
print('    '+'='*5, '< RANKING >', '='*5)
for ind, val in enumerate(ranking):
    sleep(1)
    print(f'    {ind+1}º lugar: \033[33m{val[0]}\033[m  \033[34m{val[1]}\033[m')
