from random import choice
numeros = [1,2,3,4,5,6,7,8,9,10]
vitorias = 0
while True:
    dedos = int(input('Quantos dedos jogou? '))
    escolha = str(input('Par ou Impar? [P/I]')).upper()
    computador = choice(numeros)
    resultado = computador + dedos
    if resultado % 2 == 0 and escolha == 'P' or resultado % 2 != 0 and escolha == 'I':
        print('Você ganhou!!')
        print(f'Eu escolhi {computador}')
        vitorias += 1
    else:
        break
print(f'Você perdeu, eu escolhi {computador}, porém me venceu {vitorias} vezes!!')