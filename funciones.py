def mediana_de_tres(array):
    primero = array[0]
    medio = array[len(array) // 2] #valor de la posición media del array (calcula con la división entera entre el lenght del array y 2)
    ultimo = array[-1]
    return sorted([primero, medio, ultimo])[1] #se ordena el array y se utiliza el valor medio al acceder al indice 1

def quicksort(lista):

    if len(lista) <= 1:
        return lista
    
    pivot = mediana_de_tres(lista)
    # se utiliza el concepto de comprensión de listaas para crear listaas con condiciones en una sola linea
    mayores = [x for x in lista if x > pivot]
    menores = [i for i in lista if i < pivot]
    medio = [y for y in lista if y == pivot]
    return quicksort(menores) + medio + quicksort(mayores)

def valida_entero(mensaje, error, min = float("-Inf"), max = float("Inf")):
    num = int(input(f"{mensaje}"))
    while num < min or num > max:
        num = int(input(f"{error}, {mensaje}"))
    return num


def insertion_sort(array):
    for i in range(1, len(array)):
        actual = array[i]
        j = i - 1

        # Mover hacia la derecha los elementos mayores que el actual
        while j >= 0 and array[j] > actual:
            array[j + 1] = array[j]
            j -= 1

        # Insertar el actual en la posición correcta
        array[j + 1] = actual
    return array

def busqueda_binaria(num, sorted_lista):

    izquierda = 0
    derecha = len(sorted_lista) - 1

    while izquierda <= derecha:
        medio = (izquierda + derecha) // 2
        valor_medio = sorted_lista[medio]

        if valor_medio == num:
            return medio  # Devuelve el índice donde lo encontró
        elif num < valor_medio:
            # descarta los valores más grandes y el limite derecho empieza en medio - 1 (para descartar tambien el valor de medio)
            derecha = medio - 1
        else:
            # descarta los valores mas chicos y el limite izquierdo empieza en medio + 1 (para descartar también el valor de medio)
            izquierda = medio + 1

    return -1  # No encontrado