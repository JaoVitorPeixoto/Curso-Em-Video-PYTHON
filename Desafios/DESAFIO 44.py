print('======== DESAFIO 44 ========')
print('')

produto = float(input('Informe o valor do produto para saber seu preço final: R$'))

print('''\033[7m===Informe entre 1 e 4 conforme a forma de pagamento===\033[m
\033[7m                                                       \033[m
\033[7m<1> À vista dinheiro/cheque: 10% de desconto.          \033[m
\033[7m<2> À vista no cartão:       5% de desconto.           \033[m
\033[7m<3> Em até 2x no cartão:     Preço normal.             \033[m
\033[7m<4> em 3x ou mais no cartão: 20% de juros              \033[m''')
escolha = int(input('\033[7mInforme:\033[m'))
print('-='*30)

if escolha == 1:
    preço = produto - (produto * (10/100))

elif escolha == 2:
    preço = produto - (produto * (5/100))

elif escolha == 3:
    preço = produto

elif escolha == 4:
    preço = produto + (produto * (20/100))

else:
    print('\033[31mERRO!!! INFORME UM NÚMERO ENTRE 1 E 4 CONFORME SUA ESCOLHA DE PAGAMENTO\033[m ')
    exit()

print(f'Conforme sua escolha, o preço final do produto será \033[32mR${preço:.2f}\033[m')