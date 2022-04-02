print('======== DESAFIO 27 ========')
print('')

nome = str(input('Informe seu nome: ')).strip()
print('--'*20)

nomen = nome.strip().split()
qnt = len(nomen) - 1
print(f'Olá, seja bem vindo(a) {nomen[0]} {nomen[qnt]}')