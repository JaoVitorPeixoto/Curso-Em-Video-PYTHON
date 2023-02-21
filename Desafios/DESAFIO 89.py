print('======== DESAFIO 89 ========')
print('')

from time import sleep

notas = []
aluno = []
boletim = []

c = 1
while True:
    aluno.append(str(input(f'Informe o nome do {c}º aluno: ')))
    notas.append(float(input(f'Informe a primeira nota do {c}º aluno: ')))
    notas.append(float(input(f'Informe a segunda nota do {c}º aluno: ')))
    notas.append((notas[0]+notas[1])/2)
    aluno.append(notas[:])
    boletim.append(aluno[:])
    aluno.clear()
    notas.clear()

    print('--'*30)
    esco = str(input(f'Quer continuar? [S/N]')).upper().strip()[0]
    while esco not in 'SN':
        esco = str(input(f'ERRO!! Informe corretamente, quer continuar? [S/N]')).upper().strip()[0]
    print('--'*30)
    if esco == 'N':
        print('OK! Finalizando o programa...')
        sleep(1)
        print('-='*30)
        break
    c += 1

print(f'| {"Nº":^10} | {"NOME":^10} | {"MÉDIA":^10} |')
print('\033[7m--\033[m'*20)
for c, alun in enumerate(boletim):
    print(f'\033[7m| {c:^10} | {alun[0]:^10} | \033[42m{alun[1][2]:^10}\033[m\033[7m |\033[m')
print('\033[7m--\033[m'*20)

print('')
n = 0
while True:
    n = int(input('Mostrar notas de qual aluno? [ 999 para parar ]'))

    if n == 999:
        print('Ok! Finalizando...')
        sleep(1)
        print('FIMMMNMMMMM')
        break

    while n > len(boletim)-1:
        n = int(input(f'ERRO!! Informe o \033[33mNº\033[m do aluno: '))
    sleep(1)
    print(f'Notas de {boletim[n][0]} são {boletim[n][1][:2]}')
    print('--'*30)
