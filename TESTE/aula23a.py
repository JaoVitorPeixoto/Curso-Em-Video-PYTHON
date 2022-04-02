try:
    a = int(input('Informe um número: '))
    b = int(input('Informe outro número: '))
    r = a/b
except (ValueError, TypeError):
    print('Infelizmente tivemos um problema com o tipo de dado que você informou!')

except ZeroDivisionError:
    print('O denominador não pode ser zero!!!')

except Exception as erro:
    print(f'Ocorreu um erro!!! {erro.__class__}')

except KeyboardInterrupt:
    print('Finalizou sem escrever nd.')

else:
    print(f'O resultado é {r}')

finally:
    print('Volte sempre!')