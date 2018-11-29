def resolver(aux):
    Vec_Num = []
    Vec_Sym = []
    i = 0
    x = 0
    res = 0
    pos = 0
    condicion = 0
    while x < len(aux):
        if aux[x].isdigit() or aux[x] == ".":
            try:
                Vec_Num[i] = Vec_Num[i] + aux[x]     #Concateno de haber algún elemento guardado en esa pos
            except IndexError:      # Lista vacía. Debo utlizar insert.
                Vec_Num.insert(i, aux[x])
        elif (aux[x] == "-" and not(aux[x-1].isdigit())) or (aux[x] == "-" and x == 0):   #Caso especial: 2+-3 o -2+3 por ejemplo
            try:
                Vec_Num[i] = Vec_Num[i] + aux[x]
            except IndexError:
                Vec_Num.insert(i, aux[x])
        else:
            Vec_Sym.insert(i, aux[x])            #Al detectar un símbolo se pasa a la siguiente pos
            i = i+1
        x = x+1

    for i in range(len(Vec_Num)):
        Vec_Num[i] = float(Vec_Num[i])

    Simbolos = ["^", "*", "/", "+", "-"]
    i = 0

    while condicion != 1:
        while i < len(Simbolos):
            try:
                pos = Vec_Sym.index(Simbolos[i])   #Cuando index no encuentra tira un error por eso el try except
                if Simbolos[i] == "^":
                    res = pow(Vec_Num[pos], Vec_Num[pos + 1])
                elif Simbolos[i] == "*":
                    res = Vec_Num[pos] * Vec_Num[pos + 1]
                elif Simbolos[i] == "/":
                    res = Vec_Num[pos] / Vec_Num[pos + 1]
                elif Simbolos[i] == "+":
                    res = Vec_Num[pos] + Vec_Num[pos + 1]
                elif Simbolos[i] == "-":
                    res = Vec_Num[pos] - Vec_Num[pos + 1]
                else:
                    print("No es una operación válida")

                Vec_Num[pos] = res
                Vec_Num.remove(Vec_Num[pos + 1])
                Vec_Sym.remove(Simbolos[i])
            except ZeroDivisionError:
                sys.exit("Divisón por cero")
            except ValueError:      #Cuando no encuentra el símbolo en cuestión paso al siguiente símbolo.
                i = i + 1

        condicion = 1
    return res