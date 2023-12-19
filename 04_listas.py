### Lists ###

my_list  = list ()
my_other_list = [] 

print (len(my_list))

my_list = [35, 24, 62, 52, 30, 30, 17]
print (my_list)
print (len(my_list))

my_other_list =  [18, 1.88, "Jose Luis" "Lopez"]

print (type(my_other_list))
print (type(my_list))

print (my_other_list [1]) #Imprime el valor de la posicion 1 de la lista (1.77)
print (my_other_list [-1]) #Imprime el valor de la ultima posicion de la lista (Jose Luis)
print (my_other_list [1:]) #Imprime el valor de la posicion 1 hasta el final de la lista ([1.77, 'Jose Luis'])
print (my_other_list.count (35)) #Cuenta el numero de veces que aparece el valor 35 en la lista (0)

age, height,  name,  = my_other_list
print (name)
age, height,  name,  = my_other_list [2], my_other_list [1], my_other_list [0]

print (my_list + my_other_list) #Concatena las dos listas
print ( (1, 2, 3, 4, )) #Crea una lista con los valores que le pasemos

my_list = "Hola Phyton"
print (my_list)
print (type(my_list))

my_other_list.append ("Hersill") #Añade un valor al final de la lista
print (my_other_list)

my_other_list.insert (1, "Azul") #Añade un valor en la posicion 1 de la lista
print (my_other_list)

my_other_list.remove ("Azul") #Elimina el valor "Azul" de la lista
print (my_other_list)

my_other_list.pop () #Elimina el ultimo valor de la lista
print (my_other_list)
 
my_other_list.pop (2) #Elimina el valor de la posicion 2 de la lista
print (my_other_list)

my_other_list.clear () #Elimina todos los valores de la lista
print (my_other_list)

print (my_other_list.reverse()) #Invierte el orden de la lista
print (my_other_list)

my_other_list.sort () #Ordena la lista
print (my_other_list)

print (my_other_list [1 :2]) #Imprime el valor de la posicion 1 hasta la 2 de la lista
print (my_other_list [1 :]) #Imprime el valor de la posicion 1 hasta el final de la lista

 