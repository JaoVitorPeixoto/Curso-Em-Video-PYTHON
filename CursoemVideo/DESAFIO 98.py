from time import sleep


def contador(inicio, fim, passo):
    if passo == 0:
        passo = 1
    sleep(1)
    print(f'Contagem de {inicio} até {fim} de {passo} em {passo}: ')
    if inicio > fim:
        fim -= 1
        passo *= -1
    if inicio < fim and passo < 0:
        passo *= -1
    if inicio < fim:
        fim += 1
    for c in range(inicio, fim, passo):
        print(c, end=' → ')
        sleep(0.4)
    print('Fim!')
    print('-='*30)


# Programa principal >>>>>>>>
print('======== DESAFIO 98 ========')
print('')

contador(0, 10, 1)
contador(10, 0, 2)
print('Agora é sua vez de personalizar a contagem!!')
contador(int(input('Inicío: ')), int(input('Fim: ')), int(input('Passo: ')))


