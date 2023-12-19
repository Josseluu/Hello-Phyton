### Sets ###

my_set = set ()
print (type (my_set))

my_other_set = {}
print (type (my_other_set)) #Esto no es un set, es un diccionario

my_other_set = {'Jose Luis', 'Lopez', 18} #Esto si es un set 
print (type(my_other_set))

len(my_other_set) #Devuelve el numero de elementos del set
print (len (my_other_set))

my_other_set.add ("Pepelu") #Añade un elemento al set
print (my_other_set)

print ("Jose Luis"in my_other_set) #Devuelve True si el elemento esta en el set

my_other_set.remove ("Jose Luis") #Elimina el elemento del set
print (my_other_set)

my_other_set.update ({"Fernando", "Alonso", 33}) #Añade varios elementos al set
print (my_other_set)

my_other_set.clear () #Elimina todos los elementos del set
print (my_other_set)

my_other_set = {'Jose Luis', 'Lopez', 18} #Esto si es un set
my_new_set = my_set.union (my_other_set) #Une dos sets
print (my_new_set)
