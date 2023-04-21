#mostra a soma de todos os números pares digitados
soma = 0
for c in range(1,7):
    n1 = float(input('Digite um número: '))
    if n1 % 2 == 0:
        soma += n1
print('A soma dos números digitados que são pares é {}'.format(soma))