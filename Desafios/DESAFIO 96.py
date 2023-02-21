def area(largu, compri):
    a = largu * compri
    print(f'A área do seu terreno [ {largu:.2f} x {compri:.2f} ] é {a:.2f}m²')


# Programa Principal >>>>>>>
print('======== DESAFIO 96 ========')
print('')

print(f'                    Controle de terreno     ')
print('--'*30)

area(float(input('Largura (m): ')), float(input('Comprimento (m): ')))
