n1 = float(input('Informe a nota 1: '))
n2 = float(input('Informe a nota 2: '))
m = (n1 + n2)/2
print(f'A sua media é {m:.2f}')
if m >= 6:
    print(f'Sua média {m:.2f} foi o suficiente para você ser aprovado, parabéns!!!')
else:
    print(f'A sua média {m:.2f} não foi o suficiente para você ser aprovado, estude mais!!!')