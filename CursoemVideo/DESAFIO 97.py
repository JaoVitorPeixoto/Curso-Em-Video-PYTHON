def escreva(txt):
    n = len(txt)
    print('~'*(n+n))
    print(f'{txt:^{n+n}}')
    print('~'*(n+n))


# Programa principal >>>>>>>>
print('======== DESAFIO 97 ========')
print('')

escreva(str(input('Informe qualquer coisa: ')))