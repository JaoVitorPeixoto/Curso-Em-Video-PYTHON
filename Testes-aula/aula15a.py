num = s = 0
while num != 999:
    num = int(input('Informe um número: '))
    if num == 999:
        break
    s += num
print(f'A soma é {s}.')