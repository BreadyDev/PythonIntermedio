### Lambdas ###

sumar = lambda value_1, value_2: value_1 + value_2

print(sumar(2, 4))

palindroma = lambda palabra: palabra.lower().replace(" ", "") == palabra.lower().replace(" ", "")[::-1]

print(palindroma("A luna ese anula"))

def suma_de_tres(valor):
    return lambda primer_v, segundo_v : primer_v + segundo_v + valor

print(suma_de_tres(5)(2, 4))