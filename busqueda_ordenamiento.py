import funciones as f
import random as r


num = f.valida_entero("Ingrese un número entero: ", "Por favor el número debe estar en el rango [-10000;10000] ", -10000, 10000)

length = r.randint(1, 1000) 

# se generan numeros aleatorios y el guion bajo es una convención en Python que indica que no importa el valor de la variable del bucle.
# el range es length - 1 para dejar un espacio para el numero ingresado por el usuario
lista = [r.randint(-10000, 10000) for _ in range(length - 1)] 

# se crea el indice de forma aleatoria 
index = r.randint(0, length - 1)

# se ingresa el valor del usuario en la posición aleatoria creada anteriormente
lista.insert(index, num)


# se analiza que algoritmo de ordenamiento utilizar según que tan grande sea el array
if length <= 20:
    sorted_list = f.insertion_sort(lista) 
else:
    sorted_list = f.quicksort(lista)


posicion = f.busqueda_binaria(num, sorted_list) 

if posicion == -1:
    print("No se ha encontrado el valor en la listaa")
else:
    print(f"El número ingresado ({num}) se encuentra en la posición {posicion} de la listaa")

print(f"Length del array: {length-1}")
for i in range(0, len(sorted_list)):
    print(f"key {i} ==> valor {sorted_list[i]}")

    


