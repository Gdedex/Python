#mostra a soma de todos os valores impares multiplos de 3 entre 0 e 500
soma = 0
cont = 0
for c in range(1,501,2):
    if c % 3 == 0:
        print(c)
        cont += 1
        soma += c
print('a soma dos valores é: {}'.format(soma))
print('a soma dos {} solicitados é {}'.format(cont,soma))