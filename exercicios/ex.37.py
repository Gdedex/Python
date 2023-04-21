nomevelho = ''
idadevelho = 0
idade = 0
mulheres = 0
for c in range(1,5):
    print('______{}ª PESSOA_______'.format(c))
    nome = str(input('Nome: '))
    idade = int(input('Idade: '))
    somador = idade + idade
    sexo = str(input('H ou M: ').upper())
    if sexo == 'H' and idade > idadevelho:
        idadevelho = idade
        nomevelho = nome
    if sexo == 'M' and idade < 20:
        mulheres += 1      
print('A média das idades digtadas é: {}'.format(somador/(c-1))
print('O homem mais velho é {} com {} anos de idade'.format(nomevelho, idadevelho))
print('Ao total existem {} mulheres com menos de 20 anos.'.format(mulheres))
