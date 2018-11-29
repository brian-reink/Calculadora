from Resolver_Cuenta import resolver

def encontrar_pts(string):
    i = 0
    x = 0
    y = 0
    z = 0
    pos1 = []
    pos2 = []
    fin_calculo = False

    while i < len(string):  # Encontrar todas las posiciones de los paréntesis
        if string[i] == "(":
            pos1.insert(x, i)  # (posición de la lista, posición del caracter dentro del string)
            x = x + 1
        if string[i] == ")":
            pos2.insert(y, i)
            y = y + 1
        i = i + 1
    if len(pos2) != len(pos1):  # Si hay número dispar de paréntesis.
        print("Cantidad dispar de paréntesis")
        sys.exit(-1)
    else:                     # Acá tengo que encontrar los parentesis concordantes
        while not fin_calculo:
            if len(pos1) == 0:   # Caso 0: No hay paréntesis en el string
                res = resolver(string)
                return res
            elif len(pos1) == 1:  # Caso 1: 1 solo par de paréntesis
                aux = string[pos1[0]+1:pos2[0]]
                res = str(resolver(aux))
                string = string.replace(string[pos1[0]:pos2[0]+1], res)
                res = encontrar_pts(string)
                fin_calculo = True
            elif len(pos1) == z:   # Caso 2: ((...)) el último parentesis de abertura empieza antes que el primero de cierre
                aux = string[pos1[z-1] + 1: pos2[0]]
                res = str(resolver(aux))
                string = string.replace(string[pos1[z-1]:pos2[0] + 1], res)
                res = encontrar_pts(string)
                fin_calculo = True
            elif pos1[z] > pos2[0]:   # Caso 3: (...)...(...) Hay un cierre antes de una nueva abertura
                aux = string[pos1[z-1]+1:pos2[0]]         # Dentro de este string se que no hay otro paréntesis
                # debo volver a la posición anterior de pos1 ya que la actual es mayor al pos2[0]
                res = str(resolver(aux))
                # Modifico el string con el resultado de dentro del paréntesis
                string = string.replace(string[pos1[z-1]:pos2[0]+1], res); res = encontrar_pts(string)
                fin_calculo = True
            else:
                z = z+1     # Si no es ninguno de los casos analizo el siguiente paréntesis.
    return res