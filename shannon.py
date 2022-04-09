"""
Implementar en grupos de 3 personas programas que resuelvan cada uno de los siguientes problemas:

Dado un texto, calcular códigos de Shannon-Fano que permitan comprimir el texto dado.
Dado un texto, calcular códigos de Huffman que permitan comprimir el texto dado. 
Para los dos programas, se debe informar además de la codificación, el número de bits esperado, la
entropía en el peor de los casos y el número total de bits que se necesitarían para guardar el texto dado.

Todos los programas realizados deben poder funcionar a partir de un archivo dado por el usuario. 
Los programas no pueden hacer ninguna suposición acerca del sistema operativo o del sistema de archivos del usuario. 
El archivo de entrada debe ser un archivo de texto que en una o más lineas contenga el mensaje a comprimir.
Entregar un archivo zip que contenga el código fuente de las soluciones a los problemas y un README.txt
que indique cómo se deben ejecutar los programas implementados.
"""
import sys


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
    shannon(0, n - 1, p)

    # Display the codes

    salida = "\nSimbolo\t\tProbabilidad\t\tCodigo"
    letter = p[n-1].sym
    letter = letter[::-1]
    for i in range(n - 1, -1, -1):

        temp = f"\n{letter[i]}\t\t{p[i].pro}\t"
        for j in range(p[i].top+1):
            temp += str(p[i].arr[j])
        salida += temp
    print(salida)
    with open(archivo_salida, "w") as file:
        file.write(salida)
