print('======== DESAFIO 31 ========')
print('')

print('''====================ATENÇÃO====================
Viagens com diastâncias maiores que 200km são R$0,45 por km, as demais são R$0,50''')
print('-=-='*20 + '-')

dist = int(input('Informe a distância da viagem em km: '))
if dist <= 200:
    print(f'Viagem curta, o valor a ser pago será de R${dist*0.50:.2f}')
else:
    print(f'Viagem longa, o valor a ser pago será de R${dist*0.45:.2f}')
print('Obrigado pela preferência, até a proxima.')
