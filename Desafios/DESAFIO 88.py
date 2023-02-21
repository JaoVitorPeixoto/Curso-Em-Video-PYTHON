print('======== DESAFIO 88 ========')
print('')

from random import randint
from time import sleep

jogos = []
megasena = []

print('-='*30)
print(f'{"JOGA NA MEGA SENA":^60}')
print('-='*30)

qntdjogos = int(input('Informe quantos jogos você quer sortear: '))

for jog in range(1, qntdjogos+1):
    for nums in range(0, 6):
        computador = randint(1, 60)
        if computador not in jogos:
            jogos.append(computador)

    megasena.append(jogos[:])
    jogos.clear()

print(f'-=-=-=-= SORTEANDO {qntdjogos} JOGOS -=-=-=-=')
for jog in range(0, qntdjogos):
    sleep(0.5)
    print(f'Jogo {jog+1}: {megasena[jog]}')

print('-=-=-=-= > BOA SORTE < -=-=-=-=')
