print('======== DESAFIO 12 ========')
print('')

preco = float(input('Informe o preço do produto: R$'))
desc = int(input('Informe quanto % de desconto: %'))
print('-------------------------------------------')
print('Produto: R${:.2f} \nDesconto: {}%'.format(preco, desc))
print('Valor final do produto: R${:.2f}'.format(preco-(preco*(desc/100))))
