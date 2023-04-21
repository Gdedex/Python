#compara dois números digitados
n1 = int(input('DIGITE UM NÚMERO: '))
n2 = int(input('DIGITE OUTRO NÚMERO: '))
if n1 > n2:
    print('O número {} é maior'.format(n1))
elif n2 > n1:
    print('O número {} é maior'.format(n2))
else:
    print('Os números são iguais')