def notas(*num, sit=False):
    """
    -> Função para analisar notas e situações de vários alunos.
    :param num: Uma ou mais notas de alunos (aceita várias)
    :param sit: (opicional) indicando se deve ou não adicionar a situação
    :return: Dicíonario com várias informações sobre a situação da turma
    """
    sala = {'Total': len(num), 'Maior': max(num), 'Menor': min(num), 'Média': (sum(num))/len(num)}

    if sit == True:
        if 5 <= sala['Média'] < 6:
            sala['Situação'] = 'RAZOÁVEL'

        elif sala['Média'] < 5:
            sala['Situação'] = 'RUIM'

        else:
            sala['Situação'] = 'BOA'

        return sala
    else:
        return sala




# Programa principal >>>>>>>>
print('======== DESAFIO 105 ========')
print('')

print(notas(5, 5, 8, sit=True))
help(notas)