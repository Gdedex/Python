resp = 's'
itembarato = ''
valorbarato = cont = caro = somador =  0
print('{:-^40}'.format('GERADOR DE COMPRA'))
while resp == 's':
    nome = str(input('Nome do produto: '))
    valor = float(input('Preço: R$'))
    somador += valor
    cont += 1 
    if valor > 1000:
        caro += 1
    if cont == 1:
        itembarato = nome
        valorbarato = valor
    else: 
        if valor < valorbarato:
            valorbarato = valor
            itembarato = nome
    resp = str(input('Deseja adionar mais ao carrinho? [S/N]'))
    if resp == 'n':
        break
print('{:-^40}'.format('RESULTADO DA COMPRA'))
print(f'O valor da compra foi R${somador}')
print(f'Temos {caro} itens que custam mais de R$1000.00')
print(f'O item mais barato foi {itembarato} que custou R${valorbarato:.2f}')
print('{:-^40}'.format('FIM DA COMPRA'))