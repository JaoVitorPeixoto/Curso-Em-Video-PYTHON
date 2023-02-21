print('======== DESAFIO 34 ========')
print('')

print('==========ATENÇÃO==========')
print('Para salários maiores que R$1250, um aumento de 10%, para menores, um aumento de 15%.')
print('')

salário = float(input('Informe o salário do funcionário: R$'))

if salário > 1250:
    print(f'O funcionário que recebe R${salário:.2f} terá um aumento de 10%, então passarar a receber R${salário+(salário*(10/100)):.2f}')
else:
    print(f'O funcionário que recebe R${salário:.2f} terá um aumento de 15%, então passarar a receber R${salário+(salário*(15/100)):.2f}')