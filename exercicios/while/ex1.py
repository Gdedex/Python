contador = 0
somador = 0
while True:
    n1 = int(input('Digite um número ou 999 para parar: '))
    if n1 == 999:
        break
    else:
        contador += 1
        somador += n1
print(f'A soma dos {contador} digitados foi {somador}')