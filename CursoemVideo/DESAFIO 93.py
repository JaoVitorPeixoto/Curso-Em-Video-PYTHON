print('======== DESAFIO 93 ========')
print('')

jogador = {}
jogador['Nome'] = str(input('Informe o nome do jogador: ')).strip()
jogador['Partidas'] = int(input('Informe a quantidade de partidas desse jogador: '))

print('-='*30)
gols = []
tot = 0
for c in range(1, jogador['Partidas']+1):
    gol = int(input(f'Informe a quantidade de gols na \033[33m{c}º\033[m partida: '))
    gols.append(gol)
    tot += gol

print('-='*30)
jogador['Gols por partida'] = gols[:]
jogador['Total de gols'] = tot
for key, val in jogador.items():
    print(f'{key}: {val}')

print('-='*30)
print(f'O jogador \033[4:34m{jogador["Nome"]}\033[m jogou \033[33m{jogador["Partidas"]}\033[m partidas.')
for pt, gol in enumerate(jogador['Gols por partida']):
    print(f'    → Na partida {pt+1} marcou \033[32m{gol}\033[m gols')

print(f'Foi um total de \033[33m{tot}\033[m gols.')
