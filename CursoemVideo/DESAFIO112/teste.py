print('======== DESAFIO 112 ========')
print('')

from DESAFIO112.utilidadescev import moeda, dado

n = dado.leiaDinheiro('Digite o preço: R$')
moeda.resumo(n, 80, 35)
