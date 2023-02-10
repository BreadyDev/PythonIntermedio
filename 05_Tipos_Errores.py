### Tipos de errores ### 

# Syntax error

#print "Hola mundo"
print("Hola mundo")

# Name Error

languaje = "Spanish"
print(languaje)

# Index Error

my_list = [20, 24, 62, 52, 30, 30, 17]

print(my_list[0])
print(my_list[4])
print(my_list[-1])
#print(my_list[7])

# Module not found Error

#import reduce
from functools import reduce

# KeyError

my_dict = {"Nombre": "Antonio", "Apellido": "Ramos", "Edad": 20}
print(my_dict["Edad"])
# print(my_dict["Apelido"]) # Descomentar para Error
print(my_dict["Apellido"])

# TypeError

#print(my_list["0"])
print(my_list[0])
print(my_list[False])

# ImportError

from math import pi
#from math import PI

print(pi)

# Value Error

my_int = int("10")
#my_int = int("10 años")

print(type(my_int))

# Zero Division

#print(4/0)
print(4/2)