print('======== DESAFIO 77 ========')
print('')

palavras = ('praticar', 'estudar', 'trabalhar', 'estadia', 'futuro',
            'contudo', 'contexto', 'comovente', 'programar', 'transcender')

for c in palavras:
        print(f'Na palavra \033[4:33m{c.upper()}\033[m temos:', end=' ')

        for letras in c:
            if letras.lower() in 'aeiou':
                print(letras, end=' ')

        print('\n')
