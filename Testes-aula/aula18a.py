pessoa = []
pessoa.append('Vitor')
pessoa.append(17)
galera = []
galera.append(pessoa[:])
pessoa[0] = 'Edric'
pessoa[1] = 16
galera.append(pessoa[:])

print(galera)
print(pessoa)