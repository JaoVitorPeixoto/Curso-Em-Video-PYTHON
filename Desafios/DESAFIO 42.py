print('======== DESAFIO 42 ========')
print('')

print('Informe a medida de 3 retas para saber se formam um triângulo, e qual tipo de triângulo ele forma:')

s1 = float(input('Segmento \033[34mAB\033[m: '))
s2 = float(input('Segmento \033[32mCD\033[m: '))
s3 = float(input('Segmento \033[31mEF\033[m: '))
print('-='*20)

if s1 + s2 > s3 and s1 + s3 > s2 and s2 + s3 > s1:
    if s1 == s2 == s3:
        tipo = '\033[4;33mTRIÂNGULO EQUILÁTERO\033[m'

    elif (s1 == s2 != s3) or (s1 == s3 != s2) or (s2 == s3 != s1):
        tipo = '\033[4;33mTRIÂNGULO ISÓSCELES\033[m'

    elif s1 != s2 != s3 != s1:
        tipo = '\033[4;33mTRIÂNGULO ESCALENO\033[m'

    print(f'Esses segmentos \033[32mPODEM\033[m formar um triângulo, e será um {tipo}!!')
else:
    print('Esses segmentos \033[31mNÃO PODEM\033[m formar um triângulo!!')