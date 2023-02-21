from time import sleep

qntd = int(input('Informe a quantidade de vezes que quer repetir: '))

c = 1
while c <= qntd:
    print(c, end=' ')
    c += 1
    sleep(0.5)

print('Fim!')