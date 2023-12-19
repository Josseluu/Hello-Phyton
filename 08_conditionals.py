### Conditionals ###

my_condition = False 
if my_condition: #  el if se ejecuta si la condicion es True
    print ("Se ejecuta la condicion del if") 

print("La ejecución continua") 

my_condition = 5 * 2
if my_condition == 10: #  el if se ejecuta si la condicion es True
    print ("Se ejecuta la condicion del segundo if")
    print("La ejecución continua") 

my_condition = 5 * 2
if my_condition >10: #  el if se ejecuta si la condicion es True
     print ("Es mayor que 10")
else: #  el else se ejecuta si la condicion es False
   print ("Es menor o igual que 10") 
   print("La ejecución continua") 

my_condition = 5 * 5
if my_condition >10 and my_condition <20: #  el if se ejecuta si la condicion es True
     print ("Es mayor que 10")
else: #  el else se ejecuta si la condicion es False
   print ("Es menor o igual que 10 o mayor o igual que 20") 
   print("La ejecución continua") 

my_condition = 5 * 5
if my_condition >10 and my_condition <20: #  el if se ejecuta si la condicion es True
     print ("Es mayor que 10")
elif my_condition == 1: #  el elif se ejecuta si la condicion es True
     print ("Es igual a 1")
else: #  el else se ejecuta si la condicion es False
   print ("Es menor o igual que 10 o mayor o igual que 20") 
   print("La ejecución continua") 

