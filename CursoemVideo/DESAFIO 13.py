print('======== DESAFIO 13 ========')
print('')

salario = float(input('Informe o salário do funcionário: R$'))
aumento = int(input('Informe quantos % de aumento: %'))
print('--------------------------------------------')

print('Salário: R${:.2f} \nAumento: {}%'.format(salario, aumento))
print('Novo salário: R${:.2f}'.format(salario+(salario*(aumento/100))))

