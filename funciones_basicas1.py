#1 Salida: 5 en vista de que no hay variables solo regresa el numero al momento de llamar a la funcion
def number_of_food_groups():
    return 5
print(number_of_food_groups())


#2 Salida: Error en vista de que no existe ninguna funcion number_of_days_in_a_week_or_triangle_sides()definida 
def number_of_military_branches():
    return 5
print(number_of_days_in_a_week_or_triangle_sides() + number_of_military_branches())

#3 Salida: Solo retorna el 5 en vista de que solo considera el 1er return
def number_of_books_on_hold():
    return 5
    return 10
print(number_of_books_on_hold())


#4 Salida: la funcion retorna 5 al momento de llamar la funcion. El print no lo considera porque se encuentra dentro del bloque de la funcion que ya nos está retornando el 5.
def number_of_fingers():
    return 5
    print(10)
print(number_of_fingers())


#5 Salida: se imprime solo 5, en vista de que no se declara return imprime None
def number_of_great_lakes():
    print(5)
x = number_of_great_lakes()
print(x)


#6 Salida: Error ya que intenta sumar 2 funciones en vez de los retornos de las funciones
def add(b,c):
    print(b+c)
print(add(1,2) + add(2,3))


#7 Salida: 25 por concatenar cadenas
def concatenate(b,c):
    return str(b)+str(c)
print(concatenate(2,5))


#8 Salida: imprime b que es igual a 100 y luego imprime el retorno de la funcion en else, es decir, 10. Dado que el if no se cumple.
def number_of_oceans_or_fingers_or_continents():
    b = 100
    print(b)
    if b < 10:
        return 5
    else:
        return 10
    return 7
print(number_of_oceans_or_fingers_or_continents())


#9 Salida: en vista de que las variables byc no fueron declaradas retorna 7 y 14 e imprime 21 como resultado de la suma de las funciones tomando como argumentos los retornos anteriones 
def number_of_days_in_a_week_silicon_or_triangle_sides(b,c):
    if b<c:
        return 7
    else:
        return 14
    return 3
print(number_of_days_in_a_week_silicon_or_triangle_sides(2,3))
print(number_of_days_in_a_week_silicon_or_triangle_sides(5,3))
print(number_of_days_in_a_week_silicon_or_triangle_sides(2,3) + number_of_days_in_a_week_silicon_or_triangle_sides(5,3))


#10 Retorna la suma de b+c, es decir, 8.
def addition(b,c):
    return b+c
    return 10
print(addition(3,5))



#11 Se imprime la variable b que es igual a 500, luego imprime nuevamente la variable b que es igual a 500, al momento de llamar a la funcion y asignar una nueva variable b imprime b que es igual a 300 y por ultimo se solicita imprimir el valor de la variable b fuera de la funcion, lo que es igual a 500. Salida: 500 500 300 y 500.
b = 500
print(b)
def foobar():
    b = 300
    print(b)
print(b)
foobar()
print(b)


#12 Se imprime la variable b que es igual a 500, luego imprime nuevamente la variable b que es igual a 500, al momento de llamar a la funcion y asignar una nueva variable b imprime b que es igual a 300, la funcion retorna el 300 pero como se solicita que se imprima en la consola no se muestra en la misma y por ultimo se solicita imprimir el valor de la variable b fuera de la funcion, lo que es igual a 500. Salida: 500 500 300 y 500.
b = 500
print(b)
def foobar():
    b = 300
    print(b)
    #return b
print(b)
foobar()
print(b)


#13 Se imprime la variable b que es igual a 500, luego imprime nuevamente la variable b que es igual a 500, al momento de llamar a la funcion se iguala a la nueva variable b e imprime b que es igual a 300, la funcion retorna el 300 y como ahora b es igual a lo que retorna la funcion imprime 300. Salida: 500 500 300 y 300.
b = 500
print(b)
def foobar():
    b = 300
    print(b)
    return b
print(b)
b=foobar()
print(b)


#14 Al momento de llamar a la funcion foo se imprime 1 y en vista de que la funcion foo contiene el llamado de la funcion bar declarada abajo, se imprime 3 y por ultimo se imprime 2. Salida: 1 3 2.
def foo():
    print(1)
    bar()
    print(2)
def bar():
    print(3)
foo()

#15 Al momento igualar a la funcion Y a foo y llamarla se imprime 1, luego se llama a la funcion bar que fue igualada a x y se imprime 3, luego se imprime x que es el return de la funcion bar por lo que se imprime 5 y por ultimo se imprime y que es el return de la funcion foo que es igual a 10. Salida: 1 3 5 10.
def foo():
    print(1)
    x = bar()
    print(x)
    return 10
def bar():
    print(3)
    return 5
y = foo()
print(y)
