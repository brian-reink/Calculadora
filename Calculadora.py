"""Calculadora 2.0 """
"""Conceptos Aprendidos en esta version 1.0.0:
        -Mucho manejo de strings
            +isdigit
        -Try/Except, usado para salvar errores
        -Manejo de Listas
        -Loops: While y for
        -Recursividad
        -sys: para matar al programa cuando se encuentra algún error del usuario (sys.exit())
        -Modulos, llamado de funciones y variables de otros archivos"""

import sys
from Encontrar_Parentesis import encontrar_pts

Valid_Operators = "0123456789-+*^/()"
cadena_principal = input("Buen día, porfavor ingrese su operación matemática: ")
for char in cadena_principal:
    if char not in Valid_Operators:
        sys.exit("Ha ingresado operadores inválidos o letras")
print("Res= " + "%.*f" % (4, encontrar_pts(cadena_principal)))



