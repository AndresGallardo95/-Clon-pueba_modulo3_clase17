def choose_level( p_level, n_pregunta):
    """  
    Escoge el nivel de dificultad basado en el número de pregunta y el máximo nivel permitido.  

    Dependiendo de `p_level`, la función asigna un nivel de dificultad a `n_pregunta` utilizando las siguientes reglas:  
    - Si `p_level` es 2:  
        - 'básicas' para las preguntas 1 y 2.  
        - 'intermedias' para las preguntas 3 y 4.  
        - 'avanzadas' para las preguntas 5 y 6.  
    - Si `p_level` es 3:  
        - 'básicas' para las preguntas 1, 2 y 3.  
        - 'intermedias' para las preguntas 4, 5 y 6.  
        - 'avanzadas' para las preguntas 7, 8 y 9.  

    :param n_pregunta: int, el número de pregunta actual (puede ser positivo).  
    :param p_level: int, el máximo nivel de dificultad permitido (2 o 3).  
    :return: str, el nivel de dificultad como una cadena ('basicas', 'intermedias', 'avanzadas').  

    Ejemplos:  
    >>> choose_level(2, 2)  # Devuelve 'basicas'  
    >>> choose_level(4, 2)  # Devuelve 'intermedias'  
    >>> choose_level(5, 2)  # Devuelve 'avanzadas'  
    >>> choose_level(3, 3)  # Devuelve 'basicas'  
    >>> choose_level(6, 3)  # Devuelve 'intermedias'  
    >>> choose_level(8, 3)  # Devuelve 'avanzadas'  
    """
    if p_level == 1:  
        if n_pregunta == 1:  
                level = "basicas"  # Cambiado de 'basico' a 'basicas'  
        elif n_pregunta == 2:  
                level = "intermedias"  
        elif n_pregunta == 3:  
                level = "avanzadas"  
    elif p_level == 2:  
        if 1 <= n_pregunta <= 2:  
            level = "basicas"  # Cambiado de 'basico' a 'basicas'  
        elif 3 <= n_pregunta <= 4:  
            level = "intermedias"  
        elif 5 <= n_pregunta <= 6:  
            level = "avanzadas"  
    elif p_level == 3:  
        if 1 <= n_pregunta <= 3:  
            level = "basicas"  # Cambiado de 'basico' a 'basicas'  
        elif 4 <= n_pregunta <= 6:  
            level = "intermedias"  
        elif 7 <= n_pregunta <= 9:  
            level = "avanzadas"  
    return level  


if __name__ == '__main__':
    # verificar resultados
    print(choose_level(2, 2))  # básicas
    print(choose_level(3, 2))  # intermedias
    print(choose_level(7, 2))  # avanzadas
    print(choose_level(4, 3))  # intermedias
