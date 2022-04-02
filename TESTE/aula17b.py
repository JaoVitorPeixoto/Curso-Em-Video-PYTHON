valores = []
for c in range(0, 5):
    valores.append(int(input('Informe um número: ')))

for c, v in enumerate(valores):
    if v == 2:
        print(f'2 está na posição: {c}')
