def fatorial(num=1):
    f = 1
    for c in range(num, 0, -1):
        f *= c
    return f


# Programa principal >>>>>>>
num = int(input('Informe um número para saber seu fatorial: '))
print(f'O fatorial de {num} é {fatorial(num)}')