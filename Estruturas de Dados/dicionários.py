# Uma coleção de chave-valor de tamanho flexível, em que 
# chave e valor são objetos Python

dict = {} # dicionário vazio 

d1 = {'banana': 6, 'arroz': '5Kg', 'nomes':['Matheus', 'Gabriella', 'Lesliee', 'Bruno', 'Rafael', 'Pedro', 'Karina']}
d1

#Podemos acessar valores como em listas e tuplas

d1['arroz'] # retorna o valor '5Kg'
d1['banana'] # retorna o valor 6

# Podemos acessar os valores de objeto

d1['nomes'][2] # Retorna Lesliee
d1['nomes'][0] # Retorna Matheus
d1['nomes'][-1] # Retorna Karina
d1['nomes'][-3] # Retorna Rafael
d1['nomes'] # retorna ['Matheus', 'Gabriella', 'Lesliee', 'Bruno', 'Rafael', 'Pedro', 'Karina']

# Podemos verificar se um dicionário contem uma chave

'nomes' in d1
# True

'frutas' in d1
# False

d1[5] = 'algum valor' # adicionamos um valor ao dicionário
d1

# Podemos apagar esse valor adicionado

del d1[5]
d1
# dicionário original

# MÉTODOS KEYS, VALUES

    list(d1.keys())
    # ['banana', 'arroz', 'nomes']

    list(d1.values())
    # [6,'5Kg', ['Matheus', 'Gabriella', 'Lesliee', 'Bruno', 'Rafael', 'Pedro', 'Karina']]
 
 # Podemos com valores a serem definidos, um caso comum é aquele
 # em que os valores de um dicionário são outras coleções, como listas.
 
 
 ## Por exemplo:
 
 words = ['fugir', 'estudar', 'atender', 'estudar', 'auditar', 'começar', 'visitar', 'amar']
 by_letter = {}
 
 for word in words:
     letter = word[0]
     if letter not in by_letter:
         by_letter[letter] = [word]
     else:
         by_letter[letter].append(word)
         
by_letter

# {'f': ['fugir'], 'e': ['estudar', 'estudar'], 'a': ['atender', 'auditar', 'amar'], 'c': ['começar'], 'v': ['visitar']}

# Podemos escrever o mesmo código com o método setdefault

for word in words:
    letter = word[0]
    by_letter.setdefault(letter, []).append(word)

by_letter


## CONJUNTOS

a = {1, 2, 3, 4, 5, 6, 7, 8, 9}

b = {1, 3, 5, 6, 8}

# UNIÃO

a.union(b)
# {1, 2, 3, 4, 5, 6, 7, 8, 9}

a | b
# {1, 2, 3, 4, 5, 6, 7, 8, 9}

# INTERSECÇÃO

a.intersection(b)
# {1, 3, 5, 6, 8}

a & b
# {1, 3, 5, 6, 8}

# funções de conjunto

    #.add()
    #.clear()
    #.remove()
    #.pop()
    #.union()
    #.update()
    #.intersection()
    #.intersection_update()
    #.difference()
    #.difference_update()
    #.symetric_difference()
    #.symetric_difference_update()
    #.issubset()
    #.issuperset()
    #.isdisjoint()
    
