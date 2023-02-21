print('======== DESAFIO 95 ========')
print('')

jogadores = []
jogador = {}
gols = []


c = 1
while True:
    jogador.clear()
    tot = 0
    jogador['Nome'] = str(input(f'Informe o nome do {c}º jogador: ')).strip().split()
    jogador['Partidas'] = int(input(f'Quantas partidas {jogador["Nome"][0]} jogou: '))
    for pt in range(1, jogador['Partidas']+1):
        gol = int(input(f'  Quantos gols na {pt}ª partida: '))
        tot += gol
        gols.append(gol)

    jogador['Total de gols'] = tot
    jogador['Gols por partida'] = gols[:]
    jogadores.append(jogador.copy())
    gols.clear()

    print('-='*30)
    esco = str(input('Quer continuar? [S/N]')).upper().strip()[0]
    while esco not in 'NS':
        esco = str(input('ERRO!! Informe correttamente, quer continuar? [S/N]')).upper().strip()[0]
    if esco == 'N':
        print('-='*30)
        break
    print('-='*30)
    c += 1

print(f'| {"Nº":^7} {"NOME":<7} {"GOLS":<21} {"TOTAL":>15} |')
print('--'*30)
for indice, jogad  in enumerate(jogadores):
    print(f' {indice:^7} {jogad["Nome"][0]:<7} {str(jogad["Gols por partida"]):<19} {jogad["Total de gols"]:>15}')
print('--'*30)

while True:
    num = int(input('Mostrar dados de qual jogador? [ 999 para nenhum ]'))
    while num >= len(jogadores) and num != 999:
        num = int(input(f'ERRO!! informe corretamente entre 0 e {len(jogadores) - 1}: [ 999 para nenhum ]'))

    if num == 999:
        print('-=' * 30)
        print('>>>> Programa encerrado <<<<')
        break

    print(f'-------- LEVANTAMENTO DO JOGADOR {jogadores[num]["Nome"]} --------')
    for pt, go in enumerate(jogadores[num]["Gols por partida"]):
        print(f'    → No jogo {pt+1} fez {go} gols.')
    print(f'Foi um total de {jogadores[num]["Total de gols"]} gols.')
    print('-'*49)
