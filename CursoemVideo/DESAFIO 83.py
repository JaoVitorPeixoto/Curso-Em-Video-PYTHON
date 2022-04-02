print('======== DESAFIO 82 ========')
print('')

expressao = input('Informe uma expressão para saber se ela é válida: ').strip()

cont = 0
for c in expressao:
    if c == '(':
        cont += 1

    elif c == ')':
        if cont > 0:
            cont -= 1

        else:
            cont -= 1
            break

if cont == 0:
    print('A expressão é válida!!!')
else:
    print('A expressão não é válida!!')