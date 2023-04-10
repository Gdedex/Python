dist = int(input('Distancia da viajem: '))
if dist < 200:
    valor = dist * 0.50
    print ('Para uma viajem de {:.1f}KM será cobrado o valor de: {:.2f}R$'.format(dist,valor))
else:
    valor = dist * 0.45
    print ('Para uma viajem de {:.1f}KM será cobrado o valor de: {:.2f}R$'.format(dist,valor))