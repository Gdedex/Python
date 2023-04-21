n1 = 0
while n1 >= 0:
    n1 = int(input('Digite a tabuada que deseja ver ou -1 para parar: '))
    if n1 < 0:
        break
    for c in range(0,11):
        result = n1*c
        print(f'{n1} X {c} = {result}')
print('FIM DE EXECUÇÂO')