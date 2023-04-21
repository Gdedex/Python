#mostra se o jovem deve ou não se alistar 
import datetime
nascimento = int(input('Seu ano de nascimento: '))
anoAtual =  datetime.datetime.now().year
result = anoAtual - nascimento
if result == 18:
    print('Você deve se alistar este ano')
elif result < 18:
    print('não é necessário se alistar este ano')
    print('Seu ano de alistamento será {}'.format(nascimento+18))
else:
    print('Você já deveria ter se alistado')
