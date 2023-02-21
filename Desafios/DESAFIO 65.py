print('======== DESAFIO 65 ========')
print('')

maior = soma = cont = menor = 0
escolha = ' '
while escolha not in 'N':
    num = int(input('Informe um número: '))
    soma += num
    cont += 1
    if cont == 1:
        maior = num
        menor = num

    else:
        if num > maior:
            maior = num

        elif num < menor:
            menor = num

    escolha = str(input('Quer continuar a digitar números? [S/N] ')).strip().upper()[0]
    while escolha not in 'NS':
        escolha = str(input('ERRO!! informe [S/N]: ')).strip().upper()[0]

print('-='*30)
print(f'A média dos valores informados é {soma/cont:.2f}, o menor valor é {menor:.2f} e o maior é {maior:.2f}')
