# Bucles [Python]
# Ejercicios de práctica

# Autor: Inove Coding School
# Version: 2.0

# IMPORTANTE: NO borrar los comentarios
# que aparecen en verde con el hashtag "#"

# Ejemplos con bucles "for"

colores = ['rojo', 'naranja', 'verde', 'azul']
colores_len = len(colores)

# Dado la siguiente lista de colores, utilizar "for"
# para imprimir en pantalla todos los colores
for x in colores:
    print("El color es:", x)

# Itere el "for" utilizando la lista como parámero
# y utilizar como elemento del "for" cada color
# for color ...

for color in colores:
    print("El color es:", color)

# Itere el "for" utilizando el tamaño de la lista
# como parámetro y utilizar el índice para acceder a
# los elementos de la lista
# for i ...

for x in range(colores_len):
    print("El color es:", colores[x])

print("terminamos!")