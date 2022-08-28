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