print ('Você acaba de passar pelo radar')
velocidade = int(input('Você estava a quantos KM/H: '))
if velocidade <= 80:
    print ('Continue assim...')
else:
    multa = 7*(velocidade-80)
    print ('Você foi multado por excesso de velocidade')
    print ('Deverá pagar uma multa de {:.2f}R$' .format(multa))