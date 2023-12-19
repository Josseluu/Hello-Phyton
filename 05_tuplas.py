### Tuplas ###

my_tuple = tuple ()
my_other_tuple = ()

my_tuple = (18, 1.88, "Jose Luis", "Lopez")
print (my_tuple)
print (type(my_tuple))

print (my_tuple [1]) #Imprime el valor de la posicion 1 de la tupla (1.88)
print (my_tuple [-1]) #Imprime el valor de la ultima posicion de la tupla (Lopez)
print (my_tuple [1:]) #Imprime el valor de la posicion 1 hasta el final de la tupla ((1.88, 'Jose Luis', 'Lopez'))

print (my_tuple.count (35)) #Cuenta el numero de veces que aparece el valor 35 en la tupla (0)
print (my_tuple.index ("Lopez")) #Devuelve la posicion del valor "Lopez" en la tupla (3)

my_sum_tuple = my_tuple + my_other_tuple #Concatena las dos tuplas
print (my_sum_tuple)

my_tupple = list (my_tuple) #Convierte una tupla en una lista
print (my_tupple)
print (type(my_tupple)) 

