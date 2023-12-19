### Strings ###

my_string =  "Mi String"
my_other_string = "Mi otro String"
print (len (my_string)) #Cuenta el numero de caracteres de una cadena
print (len (my_other_string)) #Cuenta el numero de caracteres de una cadena
print (my_string + " " + my_other_string) #Concatenación de cadenas de texto

my_mew_line_string = "Este es un String \ncon un salto de linea" #Salto de linea
print (my_mew_line_string)

my_tab_line_string = "Este es un String \tcon tabulación" #Tabulación
print (my_tab_line_string)

my_scape_line_string = " \t Este es un string \n escapado" #Escapado
print (my_scape_line_string)

#Formateo
name, surname, age  = "Jose Luis", "lopez" ,  18
print ("Mi nombre es {} {} y mi edad es {}".format(name, surname, age)) #Formateo de cadenas de texto
print ("Mi nombre es %s %s y mi edad es %d" % (name, surname, age)) #Formateo de cadenas de texto
print (f"Mi nombre es {name} {surname} y mi edad es {age}") 

#Desempaquetado de caracteres
language = "Phyton"
a, b, c, d, e, f = language 
print (a)
print (e)

#División
language_slice = language [1:3] #Corta la cadena de texto desde el caracter 1 al 3
print (language_slice)
language_slice = language [1:] #Corta la cadena de texto desde el caracter 1 hasta el final
print (language_slice)
language_slice = language [-2] 
print (language_slice)

#Reverse
reversed_language = language[::-1] #Invierte la cadena de texto
print (reversed_language)

#Funciones
print (language.capitalize()) #Pone la primera letra en mayuscula
print (language.upper()) #Pone todas las letras en mayuscula
print (language.lower()) #Pone todas las letras en minuscula
print (language.swapcase()) #Pone las mayusculas en minusculas y viceversa
print (language.count("h")) #Cuenta el numero de caracteres que hay entre parentesis
print (language.isnumeric ()) #Devuelve un booleano si es numerico o no
print ("1".isnumeric ()) #Devuelve un booleano si es numerico o no 
print (language.upper().isupper()) #Pone todas las letras en mayuscula y devuelve un booleano si es mayuscula o no
print (language.lower().startswith("p")) #Pone todas las letras en minuscula y devuelve un booleano si empieza por p o no