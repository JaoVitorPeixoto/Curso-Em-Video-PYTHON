from datetime import date

print('-='*50)

hoje = date.today()

ano = int(input('Informe o ano de nascimento: '))

if ano % 4 == 0 and ano % 100 == 0 or ano % 400 == 0:
    bissexto = True

else:
    bissexto = False

mes = int(input('Informe o mês de nascimento: '))

while mes <= 0 or mes > 12:
    mes = int(input('ERRO!! Informe o mês corretamente, entre <1> e <12>: '))

dia = int(input('Informe o dia de nascimento: '))
if mes == 1 or mes == 3 or mes == 5 or mes == 7 or mes == 8 or mes == 10 or mes == 12:
    while dia <= 0 or dia > 31:
        dia = int(input('ERRO!! Informe o dia corretamente, entre <1> e <31>: '))

elif mes == 4 or mes == 6 or mes == 9 or mes == 11:
    while dia <= 0 or dia > 30:
        dia = int(input('ERRO!! Informe o dia corretamente, entre <1> e <30>: '))

elif bissexto == True and mes == 2:
    while dia <= 0 or dia > 29:
        dia = int(input('ERRO!! Informe o dia corretamente, entre <1> e <29>: '))

elif bissexto == False and mes == 2:
    while dia <= 0 or dia > 28:
        dia = int(input('ERRO!! Informe o dia corretamente, entre <1> e <28>: '))

print('-='*50)

idade = (hoje.year - ano)

if hoje.day - dia == 0 and hoje.day - dia == 0:
    print(f'Você tem {hoje.year-ano} anos de vida. Sua data de nascimento: {dia}/{mes}/{ano}')

else:
    print(f'Você tem {idade-1} anos, {abs(mes-hoje.month)} mês(es) e {abs(dia-hoje.day)} dia(s) de vida. Sua data de nascimento: \033[1m{dia}/{mes}/{ano}\033[m')

