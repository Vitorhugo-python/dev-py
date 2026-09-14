
while True:
    valor1 = float(input('digite o primeiro valor: '))
    valor2 = float(input('digite o segundo valor: '))
    if valor1 > valor2:
        print('o maior valor é o valor 1: ', valor1)
    else: 
        print('o maior valor é o valor 2: ', valor2)
    if input('deseja continuar? (s/n): ') == 'n':
        break  