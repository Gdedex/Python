import random
from time import sleep
n2 = random.randint(0,5)
n1 = int(input('DIGITE O NÚMERO QUE ESTOU PENSANDO DE 0 A 5 '))
print ('PROCESSANDO...')
sleep(3)
if n1 == n2:
    print ('Você acertou')
else:
    print ('Você errou, eu escolhi o {}'.format(n2))