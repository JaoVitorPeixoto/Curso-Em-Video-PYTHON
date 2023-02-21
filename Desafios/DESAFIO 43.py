print('======== DESAFIO 43 ========')
print('')

print('''\033[7m=============TABELA IMC==============\033[m
\033[7m--Abaixo de 18.5:  ABAIXO DO PESO.   \033[m
\033[7m--Entre 18.5 e 25: PESO IDEAL.       \033[m
\033[7m--Entre 25.1 e 30: SOBREPESO.        \033[m
\033[7m--Entre 30.1 e 40: OBESIDADE.        \033[m
\033[7m--Acima de 40:     OBESIDADE MÓRBIDA.\033[m''')
print('-='*30)

print('Para saber seu IMC informe seu peso e sua altura respectivamente.')

peso = float(input('PESO: '))
altura = float(input('ALTURA: '))

imc = peso / altura**2
print('')

if imc < 18.5:
    tipo = 'é \033[33mABAIXO DO PESO\033[m, se cuide!'

elif imc >= 18.5 and imc <= 25:
    tipo = 'tem um \033[33mPESO IDEAL\033[m'

elif imc > 25 and imc <= 30:
    tipo = 'tem \033[33mSOBREPRESO\033[m, se cuide!'

elif imc > 30 and imc <= 40:
    tipo = 'tem \033[33mOBESIDADE\033[m, se cuide!'

elif imc > 40:
    tipo = 'tem \033[33mOBESIDADE MÓRBIDA\033[m, se cuide!!!'

print(f'Seu IMC é \033[34m{imc:.2f}\033[m, de acordo com a tabela você {tipo}')