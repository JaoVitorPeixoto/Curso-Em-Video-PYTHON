print('======== DESAFIO 64 ========')
print('')

print('Escreva os números para a soma, digite [ 999 ] para parar: ')
print('-='*30)

cont = 0
soma = 0
num = 0

while num != 999:
    num = float(input('Informe o número: '))
    if num == 999:
        break
    soma += num
    cont += 1

print(f'A soma de todos os {cont} números digitados é igual a {soma}')