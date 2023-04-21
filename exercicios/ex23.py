#testa se é realmente um triângulo
print('='*30)
print('Testando triângulos')
print('='*30)
lado1 = float(input('Medida do lado 1: '))
lado2 = float(input('Medida do lado 2: '))
lado3 = float(input('Medida do lado 3: '))
if lado1 > lado2 + lado3 or lado2 > lado1 + lado3 or lado3 > lado1 + lado2:
    print('Não é um triângulo!')
else:
    print('É um triângulo')