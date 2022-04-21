from suffix_array_utils import get_integer_suffix_array

"""
    2. Desarrollar una función que reciba la cadena original, el arreglo de sufijos,
    y una cadena de consulta y calcule las posiciones en las que se encuentra la cadena
    de consulta. Implementar búsqueda binaria.
"""


def obtener_cadena_de_consulta(cadena_original: str, arreglo_de_sufijos: list):
    pass


if __name__ == "__main__":
    CADENA_ORIGINAL = "algoritmos"
    suffix_array = get_integer_suffix_array(CADENA_ORIGINAL)
    obtener_cadena_de_consulta(CADENA_ORIGINAL, suffix_array)
