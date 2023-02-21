print('======== DESAFIO 20 ========')
print('')

from random import shuffle

print('====Informe os 4 alunos para sortear a ordem de apresentação====')

al1 = str(input('Aluno 1: '))
al2 = str(input('\033[31mAluno 2: \033[m'))
al3 = str(input('\033[32mAluno 3: \033[m'))
al4 = str(input('\033[33mAluno 4: \033[m'))
ordem = [al1, al2, al3, al4]

shuffle(ordem)

print('A ordem de apresentação será:')
print(f'\033[7m{ordem}\033[m')
