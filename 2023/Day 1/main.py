import sys


def main(argv):

    with open("2023/Day 1/input.txt", "r") as input:
        print(valorCalibrado(input))




def invertir(cadena):
    cadena_invertida = ""
    for i in cadena:
        cadena_invertida = i + cadena_invertida

    return cadena_invertida


def encontrarNúmero(cadena,vuelta):
    números = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]
    for n, i in enumerate(cadena):
        if i in números:
            return i
        elif vuelta:
            if i == "r" and cadena[n+1] == "u" and cadena[n+2] == "o" and cadena[n+3] == "f":
                return "4"
            elif i == "x" and cadena[n+1] == "i" and cadena[n+2] == "s":
                return "6"
            elif i == "t" and cadena[n+1] == "h" and cadena[n+2] == "g" and cadena[n+3] == "i" and cadena[n+4] == "e":
                return "8"
            elif i == "n" and cadena[n+1] == "e" and cadena[n+2] == "v" and cadena[n+3] == "e" and cadena[n+4] == "s":
                return "7"
            elif i == "o" and cadena[n+1] == "w" and cadena[n+2] == "t":
                return "2"
            elif i == "e":
                if cadena[n+1] == "e" and cadena[n+2] == "r" and cadena[n+3] == "h" and cadena[n+4] == "t":
                    return "3"
                elif cadena[n+1] == "v" and cadena[n+2] == "i" and cadena[n+3] == "f":
                    return "5"
                elif cadena[n+1] == "n":
                    if cadena[n+2] == "o":
                        return "1"
                    elif cadena[n+2] == "i" and cadena[n+3] == "n":
                        return "9"
        else:           
            if i == "o" and cadena[n+1] == "n" and cadena[n+2] == "e":
                return "1"
            elif i == "e" and cadena[n+1] == "i" and cadena[n+2] == "g" and cadena[n+3] == "h" and cadena[n+4] == "t":
                return "8"
            elif i == "n" and cadena[n+1] == "i" and cadena[n+2] == "n" and cadena[n+3] == "e":
                return "9"
            elif i == "t":
                if cadena[n+1] == "w" and cadena[n+2] == "o":
                    return "2"
                elif cadena[n+1] == "h" and cadena[n+2] == "r" and cadena[n+3] == "e" and cadena[n+4] == "e":
                    return "3"
            elif i == "f":
                if cadena[n+1] == "o" and cadena[n+2] == "u" and cadena[n+3] == "r":
                    return "4"
                elif cadena[n+1] == "i" and cadena[n+2] == "v" and cadena[n+3] == "e":
                    return "5"
            elif i == "s":
                if cadena[n+1] == "i" and cadena[n+2] == "x":
                    return "6"
                elif cadena[n+1] == "e" and cadena[n+2] == "v" and cadena[n+3] == "e" and cadena[n+4] == "n":
                    return "7"



def juntarNúmeros(línea):
    a = encontrarNúmero(línea,False)
    b = encontrarNúmero(invertir(línea), True)
    return f"{a}{b}"


def valorCalibrado(input):

    suma = 0
    for línea in input:
       suma = suma + int(juntarNúmeros(línea))
        
    return suma



if __name__ == "__main__":
    if "--test" in sys.argv:
        import doctest
        doctest.testmod(verbose=True)
    else:
        main(sys.argv)