#1) Crear una lista con los números del 1 al 100 que sean múltiplos de 4. Utilizar la función range.

multiples_of_four = list(range(4, 101, 4))
print(multiples_of_four)

#2) Crear una lista con cinco elementos (colocar los elementos que más te gusten) y mostrar el penúltimo
my_list = [True, 42, "Hello", 3.14, "World"]
print(my_list[-2])

#3)Crear una lista vacía, agregar tres palabras con append e imprimir la lista resultante por pantalla. Pista: para crear una lista vacía debes colocar los corchetes sin nada en su interior
empty_list = []
empty_list.append("hola")
empty_list.append("adios")
empty_list.append("chau")
print(empty_list)

#4)Reemplazar el segundo y último valor de la lista “animales” con las palabras “loro” y “oso”, respectivamente. Imprimir la lista resultante por pantalla.
animales = ["perro", "gato", "conejo", "pez"]
animales[1] = "loro"
animales[-1] = "oso"
print(animales)

#5)Analizar el siguiente programa y explicar con tus palabras qué es lo que realiza.

numeros = [8,15,3,22,7] # define y asigna valores a la lista numeros
numeros.remove(max(numeros)) # elimina el valor máximo de la lista numeros (22)
print(numeros) # imprime la lista ya modificada

#6) Crear una lista con números del 10 al 30 (incluído), haciendo saltos de 5 en 5 y mostrar por pantalla los dos primeros.
skip_in_five = list(range(10,31,5))
print(skip_in_five[:2])

#7) Reemplazar los dos valores centrales (índices 1 y 2) de la lista “autos” por dos nuevos valores cualesquiera.
autos = ["sedan", "polo", "suran", "gol"]
autos[1:3] = ["otro fiat cronos en la calle sin patente", " el buen fiat cronos, el mejor del 2025"]
print(autos)
#8)Crear una lista vacía llamada "dobles" y agregar el doble de 5, 10 y 15 usando append directamente. Imprimir la lista resultante por pantalla.
dobles = []
for i in range(5, 16, 5):
    dobles.append(i * 2)
print(dobles)
#9)Dada la lista “compras”, cuyos elementos representan los productos comprados pordiferentes clientes
compras = [["pan", "leche"], ["arroz", "fideos", "salsa"],["agua"]]
compras[2].append("jugo")
compras[1][1] = "tallarines"
compras[0].remove("pan")
print(compras)
#10)Elaborar una lista anidada llamada “lista_anidada” que contenga los siguientes elementos:
lista_anidada = [15,True,[25.5,57.9,30.6],False]
