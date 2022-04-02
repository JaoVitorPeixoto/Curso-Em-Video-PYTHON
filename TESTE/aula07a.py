n1 = int(input('Informe um valor: '))
n2 = int(input('Informe outro valor: '))

s = n1 + n2
sub = n1 - n2
m = n1 * n2
d = n1 / n2
di = n1 // n2
mod = n1 % n2
p = n1 ** n2

print('A soma é: {}\nA subtração é: {}\nA multiplicação é: {}\nA divisão é: {:.2f}\nA divisão inteira é: {}\nO resto da divisão é: {}\nA potência é: {}'.format(s, sub, m, d, di, mod, p))