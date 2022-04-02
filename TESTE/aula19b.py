pessoas = []
dados = {}

for c in range(1, 4):
    dados['nome'] = str(input(f'Informe o nome da {c}ª pessoa: ')).strip()
    dados['idade'] = int(input(f'Informe a idade da {c}ª pessoa: '))
    pessoas.append(dados.copy())

for pes in pessoas:
    print()
    for val in pes:
        print(val)