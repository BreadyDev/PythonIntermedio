### Funciones de Orden Superior ### 

def suma_uno(valor):
    return valor + 1

def suma_cinco(valor):
    return valor + 5

def suma_dos_valores_y_uno(primer_valor, segundo_valor, funct):
    return funct(primer_valor + segundo_valor)

print(suma_dos_valores_y_uno(5, 4, suma_uno))
print(suma_dos_valores_y_uno(5, 4, suma_cinco))

### Clousures ###

def suma_diez(original_value):
    def add(value):
        return value + 10 + original_value
    return add
    
add_closure = suma_diez(10)
print(add_closure(5))

print(suma_diez(5)(1))

### Funciones de Orden Superior - Built-in ### 

nums = [1, 5, 10, 15, 20]

# Map - ejecuta la funcion con cada elemento de la lista

def multiplicar(numero):
    return numero * 2

print(list(map(multiplicar, nums)))
print(list(map(lambda num: num * 2, nums)))

# Filter - segun si la funcion da true o false regresa el valor

def filtro_mayor_diez(num):
    if num >= 10:
        return True
    return False

print(list(filter(filtro_mayor_diez, nums)))
print(list(filter(lambda num: num >= 10, nums)))

# Reduce - Va acumulando las operaciones 
from functools import reduce

def sumar_valores(primer_valor, segundo_valor):
    return primer_valor + segundo_valor

print(reduce(sumar_valores, nums))
