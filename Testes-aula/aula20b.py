def soma(*num):
    s = c = 0
    for c in range(0, len(num)):
        s += num[c]
    return s


# Programa principal >>>>>>
print(soma(7, 7, 7, 7))