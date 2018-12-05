from Resolver_Cuenta import resolver
import sys

def encontrar_pts(string):
    char_pos = 0
    list_op_pos = 0       # Posición de la lista de posiciones de los paréntesis de apertura
    list_cl_pos = 0       # Posición de la lista de posiciones de los paréntesis de cierre
    z = 0
    op_pths_pos = []      # Posición de todos los paréntesis de apertura.
    cl_pths_pos = []      # Posición de todos los paréntesis de cierre.
    fin_calculo = False
# Llenar lista de posiciones:

    while char_pos < len(string):
        if string[char_pos] == "(":
            op_pths_pos.insert(list_op_pos, char_pos)  # (posición de la lista, posición del caracter dentro del string)
            list_op_pos = list_op_pos + 1
        if string[char_pos] == ")":
            cl_pths_pos.insert(list_cl_pos, char_pos)
            list_cl_pos = list_cl_pos + 1
        char_pos = char_pos + 1

    if len(cl_pths_pos) != len(op_pths_pos):  # Si hay número dispar de paréntesis.
        print("Cantidad dispar de paréntesis")
        sys.exit(-1)

# Encontrar los parentesis concordantes. Dependiendo el caso se procede distinto.

    else:
        while not fin_calculo:
            if len(op_pths_pos) == 0:   # Caso 0: No hay paréntesis en el string
                res = resolver(string)
                return res
            elif len(op_pths_pos) == 1:  # Caso 1: Un solo par de paréntesis
                aux = string[op_pths_pos[0]+1:cl_pths_pos[0]]
                res = str(resolver(aux))
                string = string.replace(string[op_pths_pos[0]:cl_pths_pos[0]+1], res)
                res = encontrar_pts(string)
                fin_calculo = True
            elif len(op_pths_pos) == z:   # Caso 2: ((...)) se abre un nuevo paréntesis antes del cierre del anterior.
                aux = string[op_pths_pos[z-1] + 1: cl_pths_pos[0]]  # Utilizo los paréntesis internos.
                res = str(resolver(aux))
                string = string.replace(string[op_pths_pos[z-1]:cl_pths_pos[0] + 1], res)
                # Solo quedan los paréntesis externos. -> Vuelvo a analizar.
                res = encontrar_pts(string)
                fin_calculo = True
            elif op_pths_pos[z] > cl_pths_pos[0]:   # Caso 3: (...)...(...) Hay un cierre antes de una nueva abertura
                aux = string[op_pths_pos[z-1]+1:cl_pths_pos[0]]
                # debo volver a la posición anterior de pos1 ya que la actual es mayor al pos2[0]
                res = str(resolver(aux))
                string = string.replace(string[op_pths_pos[z-1]:cl_pths_pos[0]+1], res)
                res = encontrar_pts(string)
                fin_calculo = True
            else:
                z = z+1     # Si no es ninguno de los casos analizo el siguiente paréntesis.
    return res
