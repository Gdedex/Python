#Calcula a média de um aluno
n1 = float(input('Primeira NOTA: '))
n2 = float(input('Segunda NOTA: '))
media = (n1 + n2) / 2
if media < 5: 
    print("""Aluno \033[31mREPROVADO\033[m
    média para aprovação = 7.0
    média do aluno = {}""".format(media))
elif media > 5 and media < 6.9:
    print("""Aluno de \033[31mRECUPERAÇÂO\033[m]
    média para APROVAÇÂO = 7.0
    média do ALUNO = {}""".format(media))
else:
    print("""Aluno \033[32mAPROVADO\033[mcom média {}""".format(media))
