#faz uma temporizador de 10 a 0
from time import sleep	
inicio = input('Aperte para iniciar contagem: ')
for c in range(10,0,-1):
    print(c)
    sleep(1)
print('CABOOOOOOOOOM!!!!!!')