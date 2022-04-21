from suffix_array_utils import get_integer_suffix_array

"""
    2. Desarrollar una función que reciba la cadena original, el arreglo de sufijos,
    y una cadena de consulta y calcule las posiciones en las que se encuentra la cadena
    de consulta. Implementar búsqueda binaria.
"""


def obtener_posiciones_cadena_de_consulta(cadena_original: str, arreglo_de_enteros: list, arreglo_de_sufijos: list, cadena_consulta: str):
    low = 0
    high = len(arreglo_de_enteros)-1
    mid = (high+low)//2
    answers = []

    while(high>=low):
        if arreglo_de_sufijos[mid].get("suffix").startswith(cadena_consulta):
            answers.append(arreglo_de_enteros[mid])
            break
        elif arreglo_de_sufijos[mid].get("suffix")<cadena_consulta:
            low = mid+1
        else:
            high = mid-1
        mid=(high+low)//2

    return answers


if __name__ == "__main__":
    CADENA_ORIGINAL = "esta es una cadena de algoritmos"
    parsed_original = CADENA_ORIGINAL.replace(" ", "")
    print("\nCadena original: " + CADENA_ORIGINAL)
    print("="*100)
    CADENA_CONSULTA = "es una"
    parsed_consulta = CADENA_CONSULTA.replace(" ", "")
    print("Cadena consulta: " + CADENA_CONSULTA)
    print("="*100)
    suffix_array, sortered_suffix = get_integer_suffix_array(parsed_original)
    answers = obtener_posiciones_cadena_de_consulta(parsed_original, suffix_array, sortered_suffix, parsed_consulta)
    print(answers)