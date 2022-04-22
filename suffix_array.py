import sys
from suffix_array_indexer import get_integer_suffix_array, get_integer_suffix_array_without_strings

"""
    2. Desarrollar una función que reciba la cadena original, el arreglo de sufijos,
    y una cadena de consulta y calcule las posiciones en las que se encuentra la cadena
    de consulta. Implementar búsqueda binaria.
"""


def obtener_posiciones_cadena_de_consulta(arreglo_de_enteros: list, cadena_original: str, cadena_consulta: str):
    low = 0
    high = len(arreglo_de_enteros)-1
    mid = (high+low)//2
    answers = []

    while(high >= low):
        if (cadena_original[mid:]).startswith(cadena_consulta):
            answers.append(arreglo_de_enteros[mid])
            break
        elif cadena_original[mid:] < cadena_consulta:
            low = mid+1
        else:
            high = mid-1
        mid = (high+low)//2

    return answers


if __name__ == "__main__":
    # Ruta al archivo con el texto para crearle el arreglo de sufijos
    archivo_entrada_1 = sys.argv[1]
    # Ruta al archivo con las cadenas a consultar
    archivo_entrada_2 = sys.argv[2]
    # Ruta al archivo de salida, donde se escribiran los resultados
    archivo_salida = sys.argv[3]
    # Bool para saber si imprimir o no las tablas con los sufijos
    omitir_sufijos=False
    if len(sys.argv) > 4:
        omitir_sufijos = sys.argv[4] == "--omitirEscrituraSufijos"

    # El archivo de entrada 1 expresado en un str largo sin saltos de linea
    cadena_original = ""
    with open(archivo_entrada_1, "r") as archivo_1:
        lines = archivo_1.readlines()
        for line in lines:
            cadena_original += line

    # Elimina los espacios y saltos de linea para operar mucho mas facil el str de entrada 1
    cadena_original = cadena_original.replace(" ", "")
    cadena_original = cadena_original.replace("\n", "")

    # El archivo de entrada 2 expresado en una lista de str
    cadenas_consulta = []
    with open(archivo_entrada_2, "r") as archivo_2:
        lineas = archivo_2.readlines()
        for line in lineas:
            cadenas_consulta.append(line.replace(" ", "").replace("\n", ""))

    # Escenario 1:
    suffix_array_escenario_1 = get_integer_suffix_array(cadena_original)

    # Escenario 2:
    suffix_array_escenario_2 = get_integer_suffix_array_without_strings(cadena_original)

    # Se elige arbitrariamente uno de los resultados de los dos escenarios para calcular la respuesta
    # Esto se hace porque se parte del hecho que suffix_array_escenario_1 y suffix_array_escenario_2
    # representan exactamente el mismo arreglo de sufijos, solo cambia la forma en como se obtiene
    respuesta_escenario_1 = obtener_posiciones_cadena_de_consulta(suffix_array_escenario_1, cadena_original, "cadena_consulta")


    # Writes in output file
    with open(archivo_salida, "w") as file:
        file.write(f"Respuesta al archivo '{archivo_entrada_1}' con los sufijos de '{archivo_entrada_2}':")
        file.write("\n\n")

        # Imprime para el escenario 1
        file.write("\nEscenario 1:")
        file.write("\nEn este escenario se calculan explicitamente los sufijos str.\n")
        file.write("\n\tArreglo de sufijos:\n\t" + str(suffix_array_escenario_1))
        if not omitir_sufijos:
            file.write("\n\n\tRepresentacion del arreglo de sufijos:")
            file.write("\n\t\t{:<8} {:<25}".format('Indice','Sufijo'))
            for index_1 in suffix_array_escenario_1:
                file.write("\n\t\t{:<8} {:<25}".format(index_1, cadena_original[index_1:]))
        file.write("\n\n\tRespuesta al escenario:")
        file.write("\n\t" + str(respuesta_escenario_1))
        file.write("\n\n\tEstadisticas del escenario:")
        file.write("\n\t  Longitud de caracteres de entrada: " + str(len(cadena_original)))
        file.write("\n\t  Cantidad de cadenas de consulta: " + str(len(cadenas_consulta)))
        file.write("\n\t  Cantidad de respuestas: " + str(len(respuesta_escenario_1)))
        file.write("\n\t  Espacio ocupado en el escenario: " + str(5))
        file.write("\n\t  Tiempo que se tardo: " + str(10))

        file.write("\n\n")

    print("Resultado persistido en", archivo_salida)

