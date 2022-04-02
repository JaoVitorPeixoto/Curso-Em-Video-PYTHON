print('======== DESAFIO 70 ========')
print('')

from time import sleep

c = 1
nomebarato = ''
total = maiormil = menor = 0
while True:
    nome = str(input(f'Informe o nome do {c}º produto: ')).upper().strip()
    preco = float(input(f'Informe o preço do {c}º produto: R$'))
    print('--'*30)

    total += preco

    if preco >= 1000:
        maiormil += 1

    if c == 1 or preco < menor:
        menor = preco
        nomebarato = nome

    escolha = str(input('Quer cadastrar outro produto? [S/N] ')).upper().strip()[0]
    while escolha not in 'SN':
        escolha = str(input('Erro!! digite corretamente, deseja continuar? [S/N] ')).upper().strip()[0]
    print('--'*30)

    if escolha == 'N':
        print('Finalizando programa...')
        print('-='*30)
        sleep(1)
        break

    c += 1

print(f'''O preço total de todos os produtos é \033[32mR${total:.2f}\033[m;
Em \033[33m{c}\033[m produto(os) informados, \033[33m{maiormil}\033[m tem o preço maior que R$1000;
\033[4;33m{nomebarato}\033[m é o nome do produto mais barato, custando \033[32mR${menor:.2f}\033[m''')