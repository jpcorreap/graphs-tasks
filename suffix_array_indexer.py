
"""
    Modulo utilitario encargado de indexar las cadenas
    En pocas palabras, se encarga especificamente de:

    1.2 Construir una lista de cadenas con todos los sufijos del texto original
    1.3 Ordenar la lista
    1.4 Obtener un arreglo de enteros con las posiciones de inicio de los diferentes sufijos
"""


def _get_suffix_array(string: str) -> list:
    """
        1.2. Construye una lista de objetos con las cadenas de todos los sufijos del texto original.
        Es una mejora que se hace al numeral 1.2 para obtener no solo el sufijo sino tambien
        para almacenar facilmente el indice que representa donde inicia el sufijo

        Parameters:
        -----------
            string : str
                cadena original
        
        Returns:
        -----------
            array : list
                arreglo donde cada elemento es de la forma {index, suffix}
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


def get_sorted_suffix_array(string: str) -> list:
    """
        1.3 Construye una lista de cadenas con todos los sufijos del texto original
        pero adicionalmente ordena esta lista con base en el sufijo

        Parameters:
        -----------
            string : str
                cadena original
        
        Returns:
        -----------
            array : list
                arreglo donde cada elemento es de la forma {index, suffix},
                adicionalmente, se garantiza que esta lista está ordenada
                alfabeticamente con base en el sufijo
    """
    suffix_array = _get_suffix_array(string)

    # Orders by suffix
    sorted_suffix_array = sorted(
        suffix_array,
        key=lambda x: x.get("suffix")
    )

    return sorted_suffix_array


def get_integer_suffix_array(string: str):
    """
        1.4 Construye una lista de indices de sufijos con todos los sufijos del texto original,
        esta es una lista de indices ordenados por el sufijo que representan

        Parameters:
        -----------
            string : str
                cadena original
        
        Returns:
        -----------
            array : list
                arreglo de enteros con las posiciones de inicio de los diferentes sufijos.
                Adicionalmente, se garantiza que esta lista esta ordenada
                alfabeticamente con base en el sufijo
    """
    sortered_suffix = get_sorted_suffix_array(string)
    integer_array = []

    for suffix in sortered_suffix:
        integer_array.append(suffix.get("index"))

    print("Arreglo de sufijos (solo indices):")
    print(integer_array)
    print("="*100)
    print("Arreglo de sufijos completo:")
    for line in sortered_suffix:
        print(line)

    return integer_array, sortered_suffix
