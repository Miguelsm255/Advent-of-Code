import sys


def main(argv):

    with open("2023/Day 1/input.txt", "r") as input:
        print(valorCalibrado(input))




def invertir(cadena):
    cadena_invertida = ""
    for i in cadena:
        cadena_invertida = i + cadena_invertida

    return cadena_invertida


def encontrarNúmero(cadena):
    números = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]
    for i in cadena:
        if i in números:
            return i

def juntarNúmeros(línea):
    a = encontrarNúmero(línea)
    b = encontrarNúmero(invertir(línea))
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