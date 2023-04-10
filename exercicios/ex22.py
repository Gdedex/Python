salario = float(input('Qual o salário do funcionário? R$'))
if salario <= 1250:
    aumento = salario * 0.15
    salario = salario + aumento
else:
    aumento = salario * 0.10
    salario = salario + aumento
print('o salário do funcionárioa passará a ser: R${:.2f} tendo tido um aumento de R${:.2f}'.format(salario, aumento))