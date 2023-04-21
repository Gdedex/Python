from datetime import datetime
maior = 0
menor = 0
for c in range (1,8):
    data = int(input('Em que ano a {}° pessoa nasceu? '.format(c)))
    if datetime.today().year - data < 18:
        menor += 1
    else:
        maior += 1
print('Das pessoas digitadas, {} tinham mais de 18 anos'.format(maior))
print('e {} tinham menos de 18 anos'.format(menor))