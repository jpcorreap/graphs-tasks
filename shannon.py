"""
Dado un texto, calcular codigos de Shannon-Fano que permitan comprimir el texto dado.

Se debe informar además de la codificacion, el número de bits esperado, la
entropía en el peor de los casos y el número total de bits que se necesitarían para guardar el texto dado.

El programa debe poder funcionar a partir de un archivo dado por el usuario. 
El programa no puede hacer ninguna suposicion acerca del sistema operativo o del sistema de archivos del usuario. 
El archivo de entrada debe ser un archivo de texto que en una o mas lineas contenga el mensaje a comprimir.
"""
import sys
import math

class node:
    def __init__(self) -> None:
        # for storing symbol
        self.sym = ''
        # for storing probability or frequency
        self.pro = 0.0
        self.arr = [0]*20
        self.top = 0


p = [node() for _ in range(20)]

# function to find shannon code


def shannon(l, h, p):
    pack1 = 0
    pack2 = 0
    diff1 = 0
    diff2 = 0
    if ((l + 1) == h or l == h or l > h):
        if (l == h or l > h):
            return
        p[h].top += 1
        p[h].arr[(p[h].top)] = 0
        p[l].top += 1
        p[l].arr[(p[l].top)] = 1

        return

    else:
        for i in range(l, h):
            pack1 = pack1 + p[i].pro
        pack2 = pack2 + p[h].pro
        diff1 = pack1 - pack2
        if (diff1 < 0):
            diff1 = diff1 * -1
        j = 2
        while (j != h - l + 1):
            k = h - j
            pack1 = pack2 = 0
            for i in range(l, k+1):
                pack1 = pack1 + p[i].pro
            for i in range(h, k, -1):
                pack2 = pack2 + p[i].pro
            diff2 = pack1 - pack2
            if (diff2 < 0):
                diff2 = diff2 * -1
            if (diff2 >= diff1):
                break
            diff1 = diff2
            j += 1

        k += 1
        for i in range(l, k+1):
            p[i].top += 1
            p[i].arr[(p[i].top)] = 1

        for i in range(k + 1, h+1):
            p[i].top += 1
            p[i].arr[(p[i].top)] = 0

        # Invoke shannon function
        shannon(l, k, p)
        shannon(k + 1, h, p)


# Function to sort the symbols
# based on their probability or frequency
def sortByProbability(n, p):
    temp = node()
    for j in range(1, n):
        for i in range(n - 1):
            if ((p[i].pro) > (p[i + 1].pro)):
                temp.pro = p[i].pro
                temp.sym = p[i].sym

                p[i].pro = p[i + 1].pro
                p[i].sym = p[i + 1].sym

                p[i + 1].pro = temp.pro
                p[i + 1].sym = temp.sym


if __name__ == '__main__':
    total = 0

    archivo_entrada, archivo_salida = sys.argv[1], sys.argv[2]

    test_str = ""
    with open(archivo_entrada, 'r') as archivo:
        lines = archivo.readlines()
        for line in lines:
            test_str += line

    # Estructura de diccionario donde se cuentan las apariciones de cada caracter
    all_freq = {}

    for i in test_str:
        if i in all_freq:
            all_freq[i] += 1
        else:
            all_freq[i] = 1
    # Calculo de la frecuencia de cada caracter
    for key in all_freq:
        all_freq[key] = all_freq[key] / len(test_str)

    # Input number of symbols
    n = len(all_freq)
    i = 0
    x = []
    # Input symbols
    for key in all_freq:
        ch = key
        x.append(all_freq[ch])

        # Insert the symbol to node
        p[i].sym += ch

    # Input probability of symbols
    i = 0
    for key in all_freq:
        # Insert the value to node
        p[i].pro = x[i]
        i += 1

    # Sorting the symbols based on frequency
    sortByProbability(n, p)

    for i in range(n):
        p[i].top = -1

    # Find the shannon code
    answer = shannon(0, n - 1, p)

    # Display the codes
    codes = {}
    salida = []
    letter = p[n-1].sym
    letter = letter[::-1]
    for i in range(n - 1, -1, -1):
        temp = []
        temp.append(letter[i])
        temp.append(p[i].pro)

        code = ""
        for j in range(p[i].top+1):
            code += str(p[i].arr[j])

        codes[letter[i]] = code

        temp.append(code)
        salida.append(temp)
    entr = 0

    entropia_shannon = 0
    for key in all_freq:
        entropia_shannon += (all_freq[key]*math.log2((1/all_freq[key])))

    entropia = math.log2(len(all_freq.keys()))

    # print the encoded string
    codificacion = ""
    print(codes)
    for c in test_str:
        codificacion += codes.get(c)

    # Writes in output file
    with open(archivo_salida, "w") as file:
        file.write(f"Respuesta al archivo '{archivo_entrada}' aplicando el algoritmo de Shannon-Fano")
        file.write("\n")
        file.write("\nCodificacion: " + codificacion)
        file.write("\n")
        file.write("\n{:<8} {:<25} {:<10}".format('Simbolo','Probabilidad','Codigo'))
        for line in salida:
            file.write("\n{:<8} {:<25} {:<10}".format(line[0], line[1], line[2]))
        file.write("\n")
        file.write("\nEntropia de Shannon: " + str(entropia_shannon))
        file.write("\nEntropia en el peor caso: " + str(entropia))
        file.write("\nNumero de bits esperados: " + str(entropia_shannon*len(test_str)))
        file.write(("\nNumero de bits necesarios: " + str(len(codificacion))))
