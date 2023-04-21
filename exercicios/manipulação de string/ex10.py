import random
aluno1 = input ('Nome do aluno: ')
aluno2 = input ('Nome do aluno: ')
aluno3 = input ('Nome do aluno: ')
alunos = [aluno1, aluno2, aluno3]
random.shuffle(alunos)  #embaralha uma lista
print ('a ordem de aprensentação será: {}' .format(alunos))