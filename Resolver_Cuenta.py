import sys

def resolver(string):
    Vec_Num = []
    Vec_Sym = []
    vec_pos = 0     # Posición de Vec_Num o de Vec_Sym
    x = 0           # Variable que recorre a string
    res = 0

    condicion = 0
    while x < len(string):
        if string[x].isdigit() or string[x] == ".":
            try:
                Vec_Num[vec_pos] = Vec_Num[vec_pos] + string[x]     #Concateno de haber algún elemento guardado en esa pos
            except IndexError:      # Lista vacía. Debo utlizar insert.
                Vec_Num.insert(vec_pos, string[x])
        elif (string[x] == "-" and not(string[x - 1].isdigit())) or (string[x] == "-" and x == 0):   #Caso especial: 2+-3 o -2+3 por ejemplo
            try:
                Vec_Num[vec_pos] = Vec_Num[vec_pos] + string[x]
            except IndexError:
                Vec_Num.insert(vec_pos, string[x])
        else:
            Vec_Sym.insert(vec_pos, string[x])            #Al detectar un símbolo se pasa a la siguiente pos
            vec_pos = vec_pos+1
        x = x+1

    for vec_pos in range(len(Vec_Num)):
        Vec_Num[vec_pos] = float(Vec_Num[vec_pos])

    Simbolos = ["^", "*", "/", "+", "-"]
    sym_pos = 0

    while condicion != 1:
        while sym_pos < len(Simbolos):
            try:
                pos = Vec_Sym.index(Simbolos[sym_pos])   #Cuando index no encuentra tira un error por eso el try except
                if Simbolos[sym_pos] == "^":
                    res = pow(Vec_Num[pos], Vec_Num[pos + 1])
                elif Simbolos[sym_pos] == "*":
                    res = Vec_Num[pos] * Vec_Num[pos + 1]
                elif Simbolos[sym_pos] == "/":
                    res = Vec_Num[pos] / Vec_Num[pos + 1]
                elif Simbolos[sym_pos] == "+":
                    res = Vec_Num[pos] + Vec_Num[pos + 1]
                elif Simbolos[sym_pos] == "-":
                    res = Vec_Num[pos] - Vec_Num[pos + 1]
                else:
                    print("No es una operación válida")

                Vec_Num[pos] = res
                Vec_Num.remove(Vec_Num[pos + 1])
                Vec_Sym.remove(Simbolos[sym_pos])

            except ZeroDivisionError:
                sys.exit("División por cero")
            except ValueError:      # Cuando no encuentra el símbolo en cuestión paso al siguiente símbolo.
                sym_pos = sym_pos + 1

        condicion = 1
    return res