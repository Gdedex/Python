#mostra os 10 primeiros números de uma PA
i = int(input('Primeiro número da PA: '))
r = int(input('Razão da PA: '))
decimo = i + (10-1) * r #decobrindo o 10 termo da progressão
for c in range (i , decimo , r):
    print(c)