### Diccionarios ###

my_dict = dict ()
print (type(my_dict))

my_other_dict = {} 
print (type(my_other_dict)) 

my_other_dict = {"nombre": "Jose Luis", "apellidos": "Lopez", "edad": 18, 1: "Phyton"} 
print (my_other_dict)

my_dict = {
    "nombre": "Jose Luis",
    "apellidos": "Lopez",
    "edad": 18,
    "Lenguajes ": {"Phyton", "Swift", "Java"},
    1:1.88
}
print (my_dict)
print(my_other_dict)

print(len(my_other_dict)) #Devuelve el numero de elementos del diccionario
print(len(my_dict)) #Devuelve el numero de elementos del diccionario
print (my_dict ["nombre"]) #Devuelve el valor de la clave "nombre" del diccionario
my_dict ["nombre"] = "Pepelu" #Modifica el valor de la clave "nombre" del diccionario   
print (my_dict ["nombre"]) 
my_dict ["Lenguajes "] = "Phyton", "Swift", "Java", "C++" #Añade un valor a la clave "Lenguajes" del diccionario
print (my_dict ["Lenguajes "])
my_dict.pop ("Lenguajes ") #Elimina el valor de la clave "Lenguajes" del diccionario
print (my_dict)
del my_dict [1] #Elimina el valor de la clave 1 del diccionario
print (my_dict) 

print ("Jose Luis" in my_other_dict) #Devuelve True si el elemento esta en el diccionario
print (my_dict.items ()) #Devuelve una lista con los pares clave-valor del diccionario
print (my_dict.keys()) #Devuelve una lista con las claves del diccionario
print (my_dict.values()) #Devuelve una lista con los valores del diccionario
print(my_dict.fromkeys (("Nombre, 1"))) #Devuelve un diccionario con las claves y los valores que le pasemos
print (my_dict.clear ()) #Elimina todos los elementos del diccionario 