
def cuadrado(l):
    elevados = l

    for i in range(len(elevados)):
        elevados[i] = elevados[i]**2
    print(elevados)


def cuadrado(l):
    return[x*x for x in l]


def vocales_consonantes(s):
    vocales = ["A", "E", "I", "O", "U"]
    vocalitas=''.join(vocales)
    s2 = s.upper()

    if s == s2:
        for i in range(len(s)):
            if s[i] == " ":
               print(s[i]+" ESPACIO")
            elif s[i] in vocalitas:
                print(s[i]+" VOCAL")
            else:
                print(s[i]+" CONSONANTES")
    else:
        print("Introduce mayusculas")


def suma_cuadrados(l):
    pares = 0
    for i in range(len(l)):
        if l[i]%2 == 0:
            pares = pares + l[i]**2
    return(pares)


def suma_formula(l):
    resultado = 0
    controlador = 1

    for i  in range(len(l)):
        resultado = resultado + (l[i] * controlador)
        controlador += 1
    return(resultado)


def distancia(l1, l2):
    resultado = 0
    if len(l1) == len(l2):
        for i in range(len(l1)):
            resultado = resultado + (l2[i] - l1[i])**2
        resultado = (resultado)**(1/2)
    return(resultado)



