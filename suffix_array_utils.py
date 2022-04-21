
"""
    Modulo utilitario encargado de indexar las cadenas
    En pocas palabras, se encarga especificamente de:

    1.2 Construir una lista de cadenas con todos los sufijos del texto original
    1.3 Ordenar la lista
    1.4 Escribir una función que retorne un arreglo de enteros con las posiciones de inicio de los diferentes sufijos.
"""


def _get_suffix_array(string: str) -> list:
    """
        Construye una lista de cadenas con todos los sufijos del texto original

        Parameters:
        -----------
            string : str
                cadena original
    """
    array = []
    string_len = len(string)

    i = 0
    while i < string_len:
        array.append({
            "index": i,
            "suffix": string[i:]
        })
        i += 1

    return array


def get_sorted_suffix_array(string: str):
    suffix_array = _get_suffix_array(string)

    # Orders by suffix
    sorted_suffix_array = sorted(
        suffix_array,
        key=lambda x: x.get("suffix")
    )

    return sorted_suffix_array



def get_integer_suffix_array(string: str):
    sortered_suffix = get_sorted_suffix_array(string)
    integer_array = []

    for suffix in sortered_suffix:
        integer_array.append(suffix.get("index"))

    return integer_array


suffix_int_array = get_integer_suffix_array("algoritmos") 
complete_suffix_array = get_sorted_suffix_array("algoritmos") 

print(suffix_int_array)

for line in complete_suffix_array:
    print(line)
