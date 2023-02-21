print('======== DESAFIO 72 ========')
print('')

extenso = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez', 'onze', 'doze', 'treze',
'quatorze', 'quinze', 'dezesseis', 'dezessete', 'dezoito', 'dezenove', 'vinte')

num = int(input('Informe um número entre 0 e 20 para saber ele escrito por extenso: '))

while num < 0 or num > 20:
    num = int(input('ERRO!! informe corretamente entre 0 e 20: '))

print('-='*30)
print(f'O número {num} escrito por extenso é {extenso[num]}.')

while True:
    print('-='*30)
    esc = str(input('Quer continuar? [S/N]')).strip().upper()[0]
    if esc in 'SN':

        if esc == 'S':
            print('-='*30)
            num = int(input('Informe um número entre 0 e 20 para saber ele escrito por extenso: '))

            while num < 0 or num > 20:
                num = int(input('ERRO!! informe corretamente entre 0 e 20: '))

            print(f'O número {num} escrito por extenso é {extenso[num]}.')

        elif esc == 'N':
            print('Ok!! Encerrando programa...')
            break

print('')
print('FIM')