lista1 = [ 1, 2, 3] ## lista em python
type(lista1) # >>> list 


   #       0             1          2
lista2 = [ [1,2,3] ,  [4,5,6],  [7,8,9] ]
type(lista2) # >>> list

lista1[0] ## trás o elemento de índice 0 
lista1[1] ## trás o elemento 2 de índice 1

##  filtrando o elemento dentro de um outro indice

lista2[0][0] ## retorna o elemento 1 do índice 0 de indice 0
lista2[0][1] ## retorna o elemento 2 do indice 0 e indice 1

# >>> fazemos uma filtragem dos ítens dentro da lista
select = lista2[1] ## recebe o valor [4,5,6] >>> list
select = lista2[0][1] ## recebe o valor 2 >>> int


import random
from re import S ## randomizaçao 

cidades = ['são paulo', 'santos', 'rio de janeiro', 'porto alegre']

escolhida = random.choice(cidades)
print('A cidade escolhida é: ', escolhida)


a = [ 1, 2, 3 ]

### adicionando elementos na lista

a.append(15) ### usando o método .append() do Python
print(a)
b = [7, 8, 9]

for i in b:
    a.append(i) ## o método append só inseri um valor de cada vez. Por isso     usamos o loop for para adicionar os elementos dentro de um range de uma lista
print(a)


c = [ 1, 2, (3, 4)]

# o método .pop() remove um item de índice específico 
c.pop(1)
print(c)

# o método .remove()


d = [1, 2, 3, 4, (5, 5)]
d.remove(4)

print(d)

cidades = ['são paulo', 'porto alegre', 'santos', 'bahia', 'espírito santo', 'maceió']
cidades.remove('espírito santo')
print(cidades)

# não funciona para strings - apenas para números 
cidades.remove(2)

# concatenando listas
r = ['queijo', 'leite', 'arroz']
s = ['feijão', 'cenoura', 'alface']

q = r + s
q

# o método extend insere valores a uma lista já existente
q.extend(['goiaba', 'maracujá', 'pessêgo', 'limão'])
q

# o método .sort() ordena uma lista

g = [2, 5, 4, 6, 7, 8, 13, 1]
g.sort()

print(g)

# podemos ordenar listas de acordo com o tamanho de seus elementos

names = ['Mathew', 'Bruno', 'Lucca', 'John', 'Peter', 'James']
names.sort(key=len)

names

# Fatiamento

lista = [1 , 2, 3, 4, 5, 6, 7, 8, 9]
lista[1:5] # o start:stop tem o stop como excludente

```

indice   0   1  2  3  4  5  6  7  8 
lista = [1 , 2, 3, 4, 5, 6, 7, 8, 9]
indice  -9  -8 -7 -6 -5 -4 -3 -2 -1
```

lista[:1] # retorna apenas o indice 0 pois o valor de índice 1 é excludente
lista[:] # retorna toda a lista
lista[0:5] # vai retornar os valores de índice 0 a 4
lista[3:] # retorna os valores de 4 em diante

## índices negativos

lista[-1:] # tem o último índice como parâmetro
lista[-3:] # retorna os valores de 7 à 9. O último como parâmetro 
lista[-4:-3]

lista[::-1] # ordeno a lista de trás para frente
lista[::-2] # ordena a lista de trás para frente de dois em dois
lista[::-3] # agora de três em três
lista[::-4] # de quatro em quatro

# FUNÇÃO ENUMERATE 

## neste loop for, adicionamos os índices aos valores da lista
mapping = { }
for i, v in enumerate(lista):
    mapping[v] = i
    
mapping


# um outro exemplo.
# Obs: não funcionou com outra palavra para o mapping.
# Tem que usar o mapping
# Outra observação importante é que o retorno é em tupla e não em lista
mapping = { }

for i, v in enumerate(cidades):
    mapping[v] = i
    
mapping

# {'são paulo': 0, 'porto alegre': 1, 'santos': 2, 'bahia': 3, 'maceió': 4}

# FUNÇÃO SORTED
# devolve uma nova lista ordenada a partis dos elementos de qualquer sequência:

sorted("Estudo Big Data na FATEC")

# FUNÇÃO ZIP
# "Pareia" os elementos de uma série de listas/tuplas/outras sequências
# para criar uma lista de tuplas

seq1 = ['Banana', 'Maçã', 'Mamão'] #elementos
seq2 = [6, 12, 2]  #quantidade

lista_zipada = zip(seq1, seq2)
lista_zipada
list(lista_zipada) # convertendo em lista

# podemos combinar com o enumerate

for i, (a, b) in enumerate(zip(seq1, seq2)):
    print('{0}: {1}, {2}' .format(i, a, b)) # determina o valor das colunas 1 e 2 como sendo os valores de a e b 
    
    ``` # retorno
    
    0: Banana, 6
    1: Maçã, 12
    2: Mamão, 2

    ```
    
lista_nomes = [ # lista zipada
                ('Cantarutti', 'Matheus'), 
                ('Cantarutti', 'Gustavo'), 
                ('Quinteiro', 'Gabriella')
                
              ]

# podemos "desparear" (com o unzip)

last_name, first_name = zip(*lista_nomes)

print(first_name)
# >>> ('Matheus', 'Gustavo', 'Gabriella')
print(last_name)
# >>> ('Cantarutti', 'Cantarutti', 'Quinteiro')

