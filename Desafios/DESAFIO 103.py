def ficha(nome='', gols=''):
    if gols.isnumeric():
        gols = int(gols)
    else:
        gols = 0

    if nome.strip() == '':
        return f'O jogador <desconhecido> fez {gols} gol(s) no campeonato.'
    else:
        return f'O jogador {nome} fez {gols} gol(s) no campeonato.'


# Programa principal >>>>>>>>
print('======== DESAFIO 103 ========')
print('')

nome = str(input('Informe o nome do jogador: '))
gol = str(input('Informe a quantidade de gols do jogador: '))
print('-='*30)
print(ficha(nome, gol))