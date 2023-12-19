### Operadores ###

print (3 + 4)
print (3 - 4) 
print (3 * 4)
print (3 / 4)
print (3 ** 4) #3 elevado a 4
print (10 % 5) #Resto de la división
print (10 // 5) #División entera (sin decimales)
print ( "Hola " +  "Phyton "+ "que tal " )
print ( "Hola " + str (5)) #Concatenación de un str con un int

### Operadores comparativos ###
print (3 > 4)
print (3 < 4)
print (3 >= 4)
print (3 <= 4)
print (3 == 4)
print (3 != 4) #Distinto de

print ("Hola" > "Phyton") #Compara el orden alfabético (Hola es mayor que Phyton)
print ("Hola" < "Phyton")
print ("Hola" >= "Phyton")
print ("Hola" <= "Phyton")
print ("Hola" == "Phyton")
print ("Hola" != "Phyton")
print ("Hola" >= "Zola") #Ordena el orden alfabético (Hola es menor que Zola)
print (len("aaaa")>=len("abaa")) #Compara la longitud de las cadenas por orden alfabetico


### Operadores lógicos ###
print (3 > 4 and "Hola" > "Phyton") #Logicas booleanas
print (3 > 4 or "Hola" > "Phyton")
print (3 < 4 and "Hola" < "Phyton")
print (3 < 4 or "Hola" < "Phyton")
print (3 < 4 or "Hola" > "Phyton") 
print (3 < 4 or "Hola" > "Phyton" and 4==4) #Prioridad de operadores
print (not(3 > 4)) 