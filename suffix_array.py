import sys
import time
from suffix_array_indexer import get_integer_suffix_array, get_integer_suffix_array_without_strings


def obtener_posiciones_cadena_de_consulta(cadena_original: str, arreglo_de_sufijos: list, cadena_consulta: str):
    """
        2. Desarrollar una funcion que reciba la cadena original, el arreglo de sufijos,
        y una cadena de consulta y calcule las posiciones en las que se encuentra la cadena
        de consulta. Implementar busqueda binaria.
    """
    left = 0
    right = len(arreglo_de_sufijos) - 1
    answers = []

    while left <= right:
        mid = left + (right - left) // 2
        if (cadena_original[mid:]).startswith(cadena_consulta):
            answers.append(mid)
            right = mid - 1
        elif cadena_original[mid:] < cadena_consulta:
            left = mid + 1
        else:
            right = mid - 1

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
    start_time_1 = time.time()
    suffix_array_escenario_1 = get_integer_suffix_array(cadena_original)
    respuestas_escenario_1 = []
    for cadena_consulta in cadenas_consulta:
        posiciones = obtener_posiciones_cadena_de_consulta(
            cadena_original,
            suffix_array_escenario_1,
            cadena_consulta
        )
        respuestas_escenario_1.append({
            "cadena_consulta": cadena_consulta,
            "respuesta": posiciones
        })
    end_time_1 = time.time()

    # Escenario 2:
    start_time_2 = time.time()
    suffix_array_escenario_2 = get_integer_suffix_array(cadena_original)
    respuestas_escenario_2 = []
    for cadena_consulta in cadenas_consulta:
        posiciones = obtener_posiciones_cadena_de_consulta(
            cadena_original,
            suffix_array_escenario_2,
            cadena_consulta
        )
        respuestas_escenario_2.append({
            "cadena_consulta": cadena_consulta,
            "respuesta": posiciones
        })
    end_time_2 = time.time()

    # Writes in output file
    with open(archivo_salida, "w") as file:
        file.write(f"Respuesta al archivo '{archivo_entrada_1}' con los sufijos de '{archivo_entrada_2}':")
        file.write("\n\n")

        # Imprime para el escenario 1
        file.write("Respuesta:")
        file.write("\n\tArreglo de sufijos:\n\t" + str(suffix_array_escenario_1))
        if not omitir_sufijos:
            file.write("\n\n\tRepresentacion del arreglo de sufijos:")
            file.write("\n\t\t{:<8} {:<25}".format('Indice','Sufijo'))
            for index_1 in suffix_array_escenario_1:
                file.write("\n\t\t{:<8} {:<25}".format(index_1, cadena_original[index_1:]))
        file.write("\n\n\tRespuestas:")
        for respuesta in respuestas_escenario_1:
            file.write("\n\t\t'{}': {}".format(respuesta.get("cadena_consulta"), str(respuesta.get("respuesta"))))
        
        file.write("\n\n\tEstadisticas del escenario 1:")
        file.write("\nEn este escenario se calculan explicitamente los sufijos str.\n")
        file.write("\n\t  Longitud de caracteres de entrada: " + str(len(cadena_original)))
        file.write("\n\t  Cantidad de cadenas de consulta: " + str(len(cadenas_consulta)))
        file.write("\n\t  Tiempo que se tardo: %s segundos" % (end_time_1 - start_time_1))
        file.write("\n")
        
        file.write("\n\n\tEstadisticas del escenario 2:")
        file.write("\nEn este escenario se omite el calculo explicito de los sufijos str.\n")
        file.write("\n\t  Longitud de caracteres de entrada: " + str(len(cadena_original)))
        file.write("\n\t  Cantidad de cadenas de consulta: " + str(len(cadenas_consulta)))
        file.write("\n\t  Tiempo que se tardo: %s segundos" % (end_time_2 - start_time_2))
        file.write("\n")


    print("Resultado persistido en", archivo_salida)

