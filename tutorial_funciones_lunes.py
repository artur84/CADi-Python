# -*- coding: utf-8 -*-

def cuenta_frecuencia_numeros(lista):
    """Recibe una lista de números enteros repetidos y crea una 
        tabla (dict) de la frecuencia de cada número en la lista."""

    frecuencias = dict()
    for val in lista:
        if val in frecuencias:
            frecuencias[val] += 1 # Si el valor ya esta en la tabla, acumula.
        else:
            frecuencias[val] = 1 # Si es el primero, crea la entrada.

    return frecuencias

def normaliza_tabla_frecuencias(frecs):
    """Crea una tabla de frecuencias normalizada donde la frecuencia de 
        cada valor se expresa como la fracción con respecto a la suma de
        frecuencias."""

    frecs_norm = frecs.copy()

    tot = sum(frecs.values())	# Suma de frecuencias

    # Normaliza las frecuencias.
    for val in frecs_norm.keys():
        frecs_norm[val] = frecs_norm[val] / float(tot)

    return frecs_norm

def imprime_tabla(frecs):
    """Imprime la tabla de frecuencias."""

    for val, cant in frecs.items():
        print(str(val) + ": " + str(cant))

    print(" ")

def conv_tabla_a_listas(frecs):
    """Convierte el diccionario en listas,
        Retorna dos listas: la lista de valores y la lista de 
        frecuencias."""

    return list(frecs.keys()), list(frecs.values())

def obten_set_numeros_unicos(lista):
    """Obtiene el set de numeros únicos que hay en la lista."""

    return set(lista)

if __name__ == "__main__":

    nums1 =  [1,2,2,8,8,8,8,[1,2]] 
    try:
        frecs1 = cuenta_frecuencia_numeros(nums1)
        print("frecs1")
        print(frecs1)
    except TypeError as err:
        print("It gives this error: ", err) #Unhashable type list error
    

    

    nums2 =  [1,2,2,8,8,8,8,10,3,7,7,7,7,7,'r',"r"] #it works fine
    frecs2 = cuenta_frecuencia_numeros(nums2)
    print(frecs2)

    nums3 =  [1,2,2,8,8,8,8,10,3,7,7,7,7,7,'r',"ree"] #it works fine
    frecs3 = cuenta_frecuencia_numeros(nums3)
    print(frecs3)

    imprime_tabla(frecs3)
    frecs_norm3 = normaliza_tabla_frecuencias(frecs3)
    imprime_tabla(frecs_norm3)
    #nums = [1,2,2,2,4,2,2,1,1,1,0,10,10,9,9,2,2,8,8,8,8,10,3]
    
    #frecs = cuenta_frecuencia_numeros(nums)
    #imprime_tabla(frecs)
    # frecs_norm = normaliza_tabla_frecuencias(frecs)
    # imprime_tabla(frecs_norm)

    vals, frecs_norm = conv_tabla_a_listas(frecs_norm3)
    print(vals)
    print(frecs_norm)
    # print(sum(frecs_norm))
    # print(" ")

    print(obten_set_numeros_unicos(nums3))




