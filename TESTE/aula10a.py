nome = str(input('Informe seu nome: ')).strip()
if 'JOÃO' in nome.upper() or 'VITOR' in nome.upper():
    print('Que nome lindo você tem!')
else:
    print('Seu nome é tão normal...')

print(f'Bom dia, {nome.split()[0]}', f'{nome.split()[1]}!'if(len(nome.split())-1)>=1 else'')
