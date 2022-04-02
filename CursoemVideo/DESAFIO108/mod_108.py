def aumentar(num, porc):
    resu = num + (num * (porc/100))
    return resu


def diminuir(num, porc):
    resu = num - (num * (porc/100))
    return resu


def dobro(num):
    return num * 2


def metade(num):
    return num / 2


def moeda(valor):
    return f'\033[32mR${valor:.2f}\033[m'