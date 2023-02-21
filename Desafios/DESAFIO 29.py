print('======== DESAFIO 29 ========')
print('')

from time import sleep

velo = int(input('Informe a velocidade do seu carro: '))

if velo > 80:
    print('Você foi multado por ultrapassar o limite de 80km/h!!')
    sleep(2)
    print('Processando multa...')
    sleep(3)
    print(f'A multa é de R$7.00 por km a cima do limite, então você vai pagar R${(velo-80)*7:.2f} de multa!!!')
print('-='*20)
sleep(1.2)
print('Tenha um bom dia! dirija com segurança...')