print('======== DESAFIO 35 ========')
print('')

print('Informe a medida de 3 retas para saber se formam um triângulo:')

s1 = float(input('Segmento AB: '))
s2 = float(input('Segmento CD: '))
s3 = float(input('Segmento EF: '))

if s1 + s2 > s3 and s1 + s3 > s2 and s2 + s3 > s1:
    print('Esses segmentos PODEM formam um triângulo!!!')
else:
    print('Esses segmentos NÃO PODEM formam um triângulo!!')
