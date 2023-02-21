def funcao(b):
    global a
    a = 8
    b += 5
    c = 2
    print(f'"a" dentro vale {a}')
    print(f'"b" dentro vale {b}')
    print(f'"c" dentro vale {c}')


# Programa principal >>>>>>>>

a = 5
funcao(a)
print(f'"a" fora vale {a}')