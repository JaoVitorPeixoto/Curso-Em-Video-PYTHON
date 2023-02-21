dados = {'nome': '\033[33mVitor\033[m', 'idade': 17, 'sexo': '\033[34mMasculino\033[m'}

print(dados['nome'])
print(dados['idade'])
print(dados.keys())
print(dados.values())
print(dados.items())

for keys, valores in dados.items():
    print(f'{keys} é {valores}')