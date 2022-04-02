print('======== DESAFIO 36 ========')
print('')

valorc = float(input('Informe o valor da casa: '))
salário = float(input('Informe o seu salário: '))
qntdanos = int(input('Agora informe em quantos anos você quer pagar essa casa: '))

valormensal = valorc / (qntdanos * 12)
print('-='*20)

print(f'O valor a ser pago por ano é de \033[4;33mR${valormensal:.2f}\033[m.')
print('')

if valormensal > (salário * (30/100)):
    print(f'O seu emprestimo foi \033[4;31mNEGADO!\033[m A prestação mensal a ser paga excede \033[4;33m30%\033[m do seu salário de \033[4;33mR${salário:.2f}\033[m.')

else:
    print(f'O seu emprestimo foi \033[4;32mACEITO!!\033[m, Se quiser, podemos arrumar a papelada agora mesmo!!!')