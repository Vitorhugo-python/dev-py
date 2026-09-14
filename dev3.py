#validador de senhas.


while True:
    numero = int(input('digite sua senha: '))
    senha = 202030
    if numero == senha:
        print('senha correta')
    else:
        print('senha incorreta')
    if input('deseja continuar? (s/n): ') == 'n':

        break