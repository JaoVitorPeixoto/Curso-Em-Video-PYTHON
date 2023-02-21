from random import randint
from time import sleep


def sortear(list):
    print('Sorteando 5 valores da lista ', end='')
    for c in range(0, 5):
        list.append(randint(1, 20))
        sleep(0.5)
        print(list[c], end=' ')
    sleep(1)
    print('Pronto!!')


def somaPar(list):
    s = 0
    for valor in list:
        if valor % 2 == 0:
            s += valor
    print(f'Somando os valores pares de {list}, temos {s}.')


# Programa principal >>>>>>>>
print('======== DESAFIO 100 ========')
print('')

lista = []
sortear(lista)
somaPar(lista)