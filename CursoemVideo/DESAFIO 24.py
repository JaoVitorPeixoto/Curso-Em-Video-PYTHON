print('======== DESAFIO 24 ========')
print('')

cidade = str(input('Informe o nome da cidade: ')).strip()
print('--'*20)

valida = cidade.upper().split()

print(f'O nome da cidade começa com "SANTO": {"SANTO" in valida[0]}')