def aumentar(num, porc, show=False):
    resu = num + (num * (porc/100))

    if show:
        return moeda(resu)
    else:
        return resu


def diminuir(num, porc, show=False):
    resu = num - (num * (porc/100))

    if show:
        return moeda(resu)
    else:
        return resu


def dobro(num, show=False):
    if show:
        return moeda(num * 2)
    else:
        return num * 2


def metade(num, show=False):
    if show:
        return moeda(num / 2)
    else:
        return num / 2


def moeda(valor):
    return f'\033[32mR${valor:.2f}\033[m'

