nome = str(input('digite seu nome completo:\n')).strip()
print (nome.upper()) #deixa nome em maiusculo
print (nome.lower()) #deixa nome em minusculo

print (len(nome) - nome.count(' ')) #lê o tamnho de nome sem contar os espaços
nome1 = (nome.split()) #separa cada palavra em uma lista
print (len(nome1[0]))  