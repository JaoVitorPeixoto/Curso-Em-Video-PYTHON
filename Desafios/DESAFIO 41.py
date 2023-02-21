print('======== DESAFIO 41 ========')
print('')

from datetime import date

ano_nascimento = int(input('Informe o ano de nascimento do atleta: '))
ano_atual = date.today().year
print('')

idade = ano_atual - ano_nascimento

if idade <= 9:
    print(f'O atleta tem {idade} anos, então ele é da categoria \033[4;33mMIRIM\033[m.')

elif idade <= 14:
    print(f'O atleta tem {idade} anos, então ele é da categoria \033[4;33mINFANTIl\033[m.')

elif idade <= 19:
    print(f'O atleta tem {idade} anos, então ele é da categoria \033[4;33mJUNIOR\033[m.')

elif idade <= 25:
    print(f'O atleta tem {idade} anos, então ele é da categoria \033[4;33mSÊNIOR\033[m.')

elif idade > 25:
    print(f'O atleta tem {idade} anos, então ele é da categoria \033[4;33mMASTER\033[m.')


