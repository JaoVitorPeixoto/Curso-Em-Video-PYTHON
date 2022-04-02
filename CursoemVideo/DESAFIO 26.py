print('======== DESAFIO 26 ========')
print('')

frase = str(input('Informe uma frase: ')).strip()
print('--'*20)

print(f'Quantidade de vezes que a letra "A" aparece: {frase.upper().count("A")}')
print(f'A primeira vez que "A" aparece é na posição {frase.upper().find("A")+1} e a ultima vez é na posição {frase.upper().rfind("A")+1}.')