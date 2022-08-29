# Uma tupla é uma sequência imutável, de tamanho fixo, de objetos Python.

tup = 3, 4, 5, 6
## nested tupla
nest_tupla = (4, 5, 6, 7, 8)
tup
nest_tupla

nest_tupla2 = ((1, 2, 3), (1, 2))
nest_tupla2

# podemos convertar qualquer sequência em uma tupla
# com o método tuple()

lista = [1, 23, 12, 24, 55]
tuple(lista)


tup = tuple('Matheus')
tup
# >>> ('M', 'a', 't', 'h', 'e', 'u', 's')

# podemos acessar os valores por meio do []

tup[1] # retorna 'a'
tup[0] # retorna 'M'
tup[-1] # retorna o último 's'
tup[-3] # retorna o 'e'

# podemos modificar objetos mutáveis em tuplas porem 
# as tuplas não permitem alterações depois que ela é criada

tupla = (1, 2, [3, 4], 5, 6)
tupla[0] = True

# >>> ERROR: 'tuple' object does not support item assignment

# porem podemos modificar a lista que está dentro da tupla

tupla[2].append(5)
tupla
# >>> (1, 2, [3, 4, 5], 5, 6)

# Podemos concatenar as tuplas

tupla1 = (4, None, 'comida')
tupla2 = ('Churrasco', 'amigos', 'queijo')
tupla3 = tupla1 + tupla2
tupla3
# >>> (4, None, 'comida', 'Churrasco', 'amigos', 'queijo')

# Podemos desempacotar tuplas

t = ('a', 'b', 'c')

a, b, c = t
a # saída 'a'
b # saída 'b'
c # saída 'c'

# MÉTODO COUNT: conta o nº de ocorrências de um valor
# Obs: tbm disponível em listas

t.count('c') #saída 1
