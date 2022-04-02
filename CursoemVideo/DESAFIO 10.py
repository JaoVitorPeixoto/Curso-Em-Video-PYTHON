print('======== DESAFIO 10 ========')
print('')

dinheiro = float(input('Informe quanto dinheiro você tem: R$'))
dolares = float(input('Informe quantos reais valem um dólar atualmente: R$'))
print('')
print('R${} convertido é US${:.2f}'.format(dinheiro, dinheiro/dolares))