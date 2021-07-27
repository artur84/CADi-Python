#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Programa: data_structures_prac_ex.py
Ilustra el uso de estructuras de datos.
"""

def muestra_notas(titulo, notas):
    """Imprime el titulo y las listas de notas almacenadas en
    el diccionario notas."""

    print(titulo + ": ")
    # Ejemplo de iterar en el diccionario usando .items().
    for par, lst in notas.items():
        print(str(par) + ": " + str(lst))
    print(" ")

def calcula_notas_ponderadas(ponder, notas):
    """Retorna un diccionario con las notas ponderadas para
    cada clave o parcial."""

    # Crea un diccionario de notas ponderadas 
    notas_ponder = dict()

    # Agrega la nota ponderada de cada clave o parcial:
    # 	nota_ponderada = nota * ponderacion
    for par, lst in notas.items():
        if par not in notas_ponder:
            notas_ponder[par] = [ cal * ponder[par] for cal in notas[par]]

    return notas_ponder

def calcula_nota_final(notas_ponderadas, num_calif):
    """Calcula la nota final para un diccionario (notas_ponderadas)
    donde cada clave contiene un arreglo de notas ponderadas con longitud
    num_calif"""

    # Creamos una lista de la nota_final: suma de notas ponderadas
    # por estudiante.
    nota_final = num_calif * [0.,] # Inicializamos una lista con ceros.
    for par, nota_parcial in notas_ponderadas.items():
        for i in range(0, num_calif):
            nota_final[i] += nota_parcial[i]

    return nota_final

if __name__ == "__main__":

    # Número de estudiantes y notas parciales.
    n_estud = 7
    notas = {
            "parcial1": [95., 83., 98., 90., 70., 88., 95.],
            "parcial2": [99., 85., 90., 85., 80., 90., 95.],
            "proyecto": [97., 88., 95., 97., 90., 85., 90.],
            "ex_final": [94., 90., 90., 92., 85., 88., 100.]
        }

    # Ponderación
    ponderacion = dict([("parcial1", 0.25), ("parcial2",0.25), \
                        ("proyecto",0.4), ("ex_final",0.1)])

    # Mostramos las notas parciales iterando por las claves.
    print(" ")
    print("notas parciales: ")
    for par in notas.keys():
        print(par + ": " + str(notas[par]))
    print(" ")

    # Mostramos directamente el diccionario por su tamaño.
    print("ponderacion: ")
    print(str(ponderacion))
    print(" ")

    # Mostramos las notas ponderadas.
    notas_ponderadas = calcula_notas_ponderadas(ponderacion, notas)
    muestra_notas("notas ponderadas", notas_ponderadas)

    # Calcula la nota final
    nota_final = calcula_nota_final(notas_ponderadas, n_estud)

    # Agregamos la nota final al diccionario utilizando .update().
    notas.update({"nota_final": nota_final})

    # Mostramos las notas finales.
    muestra_notas("notas finales", notas)
    print(" ")