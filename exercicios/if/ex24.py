print('SIMULADOR DE EMPRÉSTIMO IMOBILIÁRIO')
vcasa = float(input('Valor do Imóvel: R$'))
salario = float(input('Digite seu salário: R$'))
tempo = int(input('Pagará em quantos anos?\n'))
tempo = tempo * 12
mensalidade = vcasa/tempo
if mensalidade > salario + (salario * 0.30):
    print('O empréstimo foi negado')
    print('O valor das parcelas mensais é 30% maior que o salário infomado')
else:
    print('O empréstimo será concedido')
    print('O valor das parcelas mensais será de R${:.2f}'.format(mensalidade))