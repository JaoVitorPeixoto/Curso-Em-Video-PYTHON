print('======== DESAFIO 109 ========')
print('')

from DESAFIO109 import mod_109

n = float(input('Digite o preço: R$'))
print('--'*30)

print(f'Aumentando 10% de {mod_109.moeda(n)}, temos {mod_109.aumentar(n, 10, True)}')
print(f'Reduzindo 13% de {mod_109.moeda(n)}, temos {mod_109.diminuir(n, 13, True)}')
print(f'O dobro de {mod_109.moeda(n)} é {mod_109.dobro(n, True)}')
print(f'A metade de {mod_109.moeda(n)} é {mod_109.metade(n, True)}')