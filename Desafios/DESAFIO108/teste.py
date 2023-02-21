print('======== DESAFIO 108 ========')
print('')

from DESAFIO108 import mod_108

n = float(input('Digite o preço: R$'))
print('--'*30)

print(f'Aumentando 10% de {mod_108.moeda(n)}, temos {mod_108.moeda(mod_108.aumentar(n, 10))}')
print(f'Reduzindo 13% de {mod_108.moeda(n)}, temos {mod_108.moeda(mod_108.diminuir(n, 13))}')
print(f'O dobro de {mod_108.moeda(n)} é {mod_108.moeda(mod_108.dobro(n))}')
print(f'A metade de {mod_108.moeda(n)} é {mod_108.moeda(mod_108.metade(n))}')