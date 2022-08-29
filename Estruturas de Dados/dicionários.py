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
 
 