#Variables
my_string_variable = "My String variable"
print (my_string_variable)

my_int_variable = "5"
print (my_int_variable)

my_int_to_str_variable =str(my_int_variable)
print (my_int_to_str_variable)
print (type(my_int_to_str_variable))

my_bool_variable = "False"
print (my_bool_variable)

#Concatenación de variables en un print
print (my_string_variable,str(my_int_to_str_variable),my_bool_variable)
print ("Este es el valor de:", my_bool_variable)

#Funciones del sistema
print (len(my_string_variable))  #Cuenta el numero de caracteres de una cadena

#Variables en una sola linea
name, surname, alias, age = "Jose Luis", "Lopez", "Pepelu", 18
print ("Me llamo:", name, surname,"Mi alias es:", alias, "Mi edad es :" ,age)

#Inpunts
name = input("Introduce tu nombre: ")   
age = input("Introduce tu edad: ")  
print (name)
print (age)

