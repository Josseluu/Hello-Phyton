### Loops ### o ###Bucles ###

#While

my_condition = 0
while my_condition < 20: #  el while se ejecuta si la condicion es True y para cuando es False
    print (my_condition)
    my_condition +=1 #Incrementa en 2 el valor de la variable my_condition
    if my_condition == 10: #  el if se ejecuta si la condicion es True
        print ("mi condicion es igual a 10")
        break #  el break se ejecuta si la condicion es True y para el while
else : #  el else se ejecuta si la condicion es False
 print ("El valor de my_condition es mayor o igual que 10") 
    
print("La ejecución continua")

#For

my_list = [1,2,3,4,5,6,7,8,9,10] 
for element in my_list: #  el for se ejecuta si la condicion es True y para cuando es False
    print (element)
my_tuple = (18, 1.88, "Jose Luis", "Lopez")
for element in my_tuple: #  el for se ejecuta si la condicion es True y para cuando es False
    print (element)
my_set = {'Jose Luis', 'Lopez', 18} 
for element in my_set: #  el for se ejecuta si la condicion es True y para cuando es False
    print (element)
 
else: #  el else se ejecuta si la condicion es False
    print ("No hay mas elementos en la lista")

my_dict = {'Jose Luis': 18, 'Lopez': 1.88, 'Pepelu': 33}
for element in my_dict: #  el for se ejecuta si la condicion es True y para cuando es False
    print (element)
    break #  el break se ejecuta si la condicion es True y para el for
else: #  el else se ejecuta si la condicion es False
    print ("No hay mas elementos en la lista")
