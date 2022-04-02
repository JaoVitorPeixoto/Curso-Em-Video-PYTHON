print('======== DESAFIO 53 ========')
print('')

frase = str(input('Informe uma frase para saber se ela é palíndroma ou não: ')).strip()

rfrase =''
for c in range(len(frase.replace(' ', ''))-1, -1, -1):
    rfrase = rfrase + frase.replace(' ', '')[c]


print('-='*30)
if rfrase.replace(' ', '').upper() == frase.replace(' ', '').upper():
    print(f'A frase \033[4;33m{frase.replace(" ", "")}\033[m é igual a \033[4;33m{rfrase.replace(" ", "")}\033[m, ela mesma lida de trás para frente, então \033[4;32mELA É PALÍNDROMA!\033[m')

else:
   print(f'A frase \033[4;33m{frase.replace(" ", "")}\033[m é diferente de \033[4;33m{rfrase.replace(" ", "")}\033[m, ela mesma lida de trás para frente, então \033[4;31mELA NÃO É PALÍNDROMA!\033[m')

