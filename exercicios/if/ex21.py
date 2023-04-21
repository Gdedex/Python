n1 = int(input('digite um número: '))
n2 = int(input('digite outro número: '))
n3 = int(input('digite outro número: '))
menor = n1 #descobrindo o menor
if n2 < n1 and n2 < n3:
    menor = n2
if n3 < n2 and n3 < n1:
    menor = n3

maior = n2 #descobrindo o maior
if n1 > n2 and n1 > n3:
    maior = n1
if n3 > n1 and n3 > n2:
    maior = n3
print('o menor número é: {}'.format(menor))
print('o maior número é: {}'.format(maior))
