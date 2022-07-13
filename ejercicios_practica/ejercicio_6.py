# Bucles [Python]
# Ejercicios de práctica

# Autor: Inove Coding School
# Version: 2.0

# IMPORTANTE: NO borrar los comentarios
# que aparecen en verde con el hashtag "#"

# Ejercicio de secuencias numéricas

# Pedir por consola dos números que representen el principio y fin de una
# secuencia numérica.
# Realizar un bucle "for" que recorra esa secuencia armada con "range"
# y cuante cuantes números son negativos y cuantos números son mayor o igual a cero
# Tener en cuenta que "range" no incluye el número de "fin" en su secuencia,
# sino que va hasta el anterior

inicio = int(input('Ingrese el primer número de la secuencia\n'))
fin = int(input('Ingrese el último número de la secuencia\n'))

cantidad_positivos = 0  # Inicializo el contador en 0
cantidad_negativos = 0
# for ... in range(....)
if inicio < fin:
    for numero in range( inicio, fin +1):
        if numero >= 0:
            cantidad_positivos = cantidad_positivos + 1
        else:
            cantidad_negativos = cantidad_negativos + 1    
    print("La cantidad de numeros mayores a 0 es:", cantidad_positivos, )
    print("La cantidad de numeros negativos es:", cantidad_negativos)

else:
    print("El primer numero ingresado tiene que ser menor al segundo numero ingresado")
# Imprimir el valor de la cantidad de números positivos y negativos

print("terminamos!")
