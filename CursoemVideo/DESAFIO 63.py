print('======== DESAFIO 63 ========')
print('')

print('-='*30)
print('SEQUÊNCIA DE FIBONACCI: ')
print('-='*30)

num = int(input('Informe a quantidade de termos que você quer mostrar: '))
print('~~'*30)

c = 0
t1 = 0
t2 = 1

print(f'{t1} → {t2} → ', end='')
while c < num:
    t3 = t1 + t2
    print(f'{t3} → ', end='')
    t1 = t2
    t2 = t3
    c += 1
print('FIM')
print('\n'+'~~'*30)
