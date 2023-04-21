import random
aluno1 = input ('Nome do aluno: ')
aluno2 = input ('Nome do aluno: ')
aluno3 = input ('Nome do aluno: ')
alunos = [aluno1,aluno2,aluno3] #cria uma lista de variaveis
print ('O aluno escolhido entre {}, {}, {} foi {}' .format(aluno1, aluno2, aluno3, random.choice(alunos))) #escolhe aleatoriamente um nome da lista