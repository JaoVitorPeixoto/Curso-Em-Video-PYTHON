def fatorial(n, show=False):
    """
    -> Função para mostrar fatorial com ou sem calculo.
    :param n: Número para ver seu fatorial
    :param show: (Opicional) "True" irá retorna o calculo, "False" não
    :return: Retorna o valor fatorial de n
    FUNÇÃO FEITA POR JOÃO VITOR DO IFBA.
    """
    f = 1
    if show == True:
        for c in range(n, 0, -1):
            f *= c
            print(f'{c}', end=' x ' if c != 1 else f' = ')
        return f

    else:
        for c in range(n, 0, -1):
            f *= c
        return f


# Programa principal >>>>>>>>
print('======== DESAFIO 102 ========')
print('')

n = int(input('Informe um número para saber seu fatorial: '))
print(f'O fatorial de {n} é :', end=' ')
print(fatorial(n, True))
