
"""
    Modulo utilitario encargado de indexar las cadenas
    En pocas palabras, se encarga especificamente de:

    1.2 Construir una lista de cadenas con todos los sufijos del texto original
    1.3 Ordenar la lista
    1.4 Obtener un arreglo de enteros con las posiciones de inicio de los diferentes sufijos
    3.  Modificar la construcción del arreglo de sufijos para generar el arreglo ordenado de
        posiciones sin tener que calcular explicitamente los sufijos.
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


def get_integer_suffix_array(string: str) -> list:
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

    return integer_array


def get_integer_suffix_array_without_strings(string: str) -> list:
    """
        3. Construye una lista de indices de sufijos con todos los sufijos del texto original,
        retorna exactamente lo mismo que get_sorted_suffix_array pero con la excepcion de que
        en esta funcion no se declaran explicitamente los sufijos, sino que solo se opera con
        enteros que representan los indices de donde empiezan los sufijos

        Parameters:
        -----------
            string : str
                cadena original

        Returns:
        -----------
            array : list
                arreglo de enteros con las posiciones de inicio de los diferentes sufijos.
                Adicionalmente, se garantiza que esta lista esta ordenada alfabeticamente con
                base en el sufijo que representan
    """
    # Calcular todos los sufijos se reduce a tener todos los posibles indices
    integer_array = [x for x in range(len(string))]
    
    sorted_integer_array = sorted(
        integer_array,
        key=lambda i: string[i:]
    )

    return sorted_integer_array

get_integer_suffix_array_without_strings("esta es una cadena de algoritmos")
