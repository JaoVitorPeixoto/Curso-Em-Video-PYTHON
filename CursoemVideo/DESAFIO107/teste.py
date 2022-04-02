print('======== DESAFIO 107 ========')
print('')

from DESAFIO107 import mod_107

n = float(input('Digite o preço: R$'))
print('--'*30)

print(f'Aumentando 10% de {n}, temos {mod_107.aumentar(n, 10)}')
print(f'Reduzindo 13% de {n}, temos {mod_107.diminuir(n, 13)}')
print(f'O dobro de {n} é {mod_107.dobro(n)}')
print(f'A metade de {n} é {mod_107.metade(n)}')