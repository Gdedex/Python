escolha = 1
while escolha == 1:
    num1 = int(input('Digite um número: '))
    print("""Escolha uma das opções abaixo
    [1] para converter em binário
    [2] para converter em octal
    [3] para converter em hexadecimal""")
    opcao = int(input('Escolha: '))
    if opcao == 1:
        print('{} em BINÁRIO é {}'.format(num1, bin(num1)))
    elif opcao == 2:
        print('{} em OCTAL é {}'.format(num1, oct(num1)))
    else:
        print('{} em HEXADECIAML é {}'.format(num1, hex(num1)))
    escolha = int(input("""Digite 1 para repetir ou
0 para sair..."""))