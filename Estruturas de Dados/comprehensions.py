# O list comprehensions permitem que você componha uma nova lida de modo conciso,
# filtrando os elementos de uma coleção, transformando os elementos ao passar o filtro
# com uma expressão concisa

# Formato básico:
# [expr for val in collection if condition]

# Equivalente à:

#    result = []
#    for val in collection:
#        if condition:
#            result.append(expr)