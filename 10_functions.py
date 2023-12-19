### Funciones ###

def my_function(): #  Definicion de la funcion
    print ("Esto es una función")
my_function() #  Llamada a la funcion

def my_function_with_arguments (first_argument, second_argument): #  Definicion de la funcion
    print (first_argument + second_argument) #  Imprime el resultado de la suma de los argumentos
my_function_with_arguments (5, 25) #  Llamada a la funcion

def sum_two_values (first_number, second_number): #  Definicion de la funcion
    return first_number + second_number #  Devuelve el resultado de la suma
print (sum_two_values (5, 5)) #  Llamada a la funcion
print (sum_two_values (390, 5)) #  Llamada a la funcion
print (sum_two_values ("5", "5")) #Se juntan los valores en vez de sumarse

def sum_two_values (first_number, second_number): #  Definicion de la funcion
    my_sum = first_number + second_number #  Devuelve el resultado de la suma
    return my_sum
print (sum_two_values (5, 33)) #  Llamada a la funcion

def print_name (name, surname):
    print (f"{name} {surname}")

print_name("Lopez", "Jose Luis")
print_name (surname = "Lopez", name = "Jose Luis")
 
def print_name_with_default (name, surname,alias ): # Si no pongo pepelu pone el valor por defecto
    print (f"{name} {surname} {alias}") 
print_name_with_default ("Jose Luis", "Lopez","Pepelu" ) 

def print_name_with_default (name, surname,alias = "Sin alias"): # Si no pongo pepelu pone el valor por defecto
    print (f"{name} {surname} {alias}") 
print_name_with_default ("Jose Luis", "Lopez", ) 

def print_texts(*text): # Uso * cuando pongo varios argume
    print (text)
    
print_texts("Hola", "Phyton")