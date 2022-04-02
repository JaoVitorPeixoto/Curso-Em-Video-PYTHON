print('======== DESAFIO 22 ========')
print('')

nome = str(input('Informe seu nome: ')).strip()
print('--'*40)


print(f'Seu nome com letras maiúsculas: {nome.upper():=^40}')
print(f'Seu nome com letras minúsculas: {nome.lower():=^40}')

print(f'A quantidade de letras é: {len(nome.replace(" ", ""))}')
print(f'Quantidade de letras do primeiro nome é: {len(nome.split()[0])}')


