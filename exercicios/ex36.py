peso = 0.0
maior = 0.0
menor = 0.0

for c in range(1,6):
    menor = float(input('Peso da {}ª pessoa: '.format(c)))
    if menor < menor:
        menor = menor
    elif menor > maior:
        maior = menor
print('O menor peso digitado foi {}Kg'.format(menor))
print('O maior peso digitado foi {}Kg'.format(maior))
    