#mostra a tabuada de um número
n1 = int(input('Deseja ver qual tabuada?'))
for c in range(1,11):
    print('{} X {} = {}'.format(n1, c, n1 * c))