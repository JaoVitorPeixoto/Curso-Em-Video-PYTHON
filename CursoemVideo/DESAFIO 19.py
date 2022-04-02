print('======== DESAFIO 19 ========')
print('')

from random import choice

print('=======Informe o nome dos alunos a serem sorteados=======')
al1 = str(input('Aluno 1: '))
al2 = str(input('Aluno 2: '))
al3 = str(input('Aluno 3: '))
al4 = str(input('Aluno 4: '))
lista = [al1, al2, al3, al4]

print(f'===Tabela de alunos===\n{al1}\n{al2:}\n{al3:}\n{al4:}')
print('='*23)

print(f'Quem vai apagar o quadro é >>>>>>>>>{choice(lista)}<<<<<<<<<')
