def votar(nasc):
    from datetime import date

    idade = date.today().year - nasc
    if idade < 16:
        return f'A idade é {idade}: \033[31m VOTO NEGADO\033[m.'

    elif 18 > idade >= 16:
        return f'A idade é {idade}: \033[33m VOTO OPICIONAL\033[m.'

    elif 18 <= idade < 65:
        return f'A idade é {idade}: \033[32m VOTO OBRIGATÓRIO\033[m.'

    else:
        return f'A idade é {idade}: \033[33m VOTO OPICIONAL\033[m.'


# Programa principal >>>>>>>>
print('======== DESAFIO 101 ========')
print('')

nascimento = int(input('Informe a data de nascimento: '))
print(votar(nascimento))