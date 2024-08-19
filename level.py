def choose_level(n_pregunta, p_level):
    """  
    Escoge el nivel de dificultad basado en el número de pregunta y el máximo nivel permitido.  

    Dependiendo de `p_level`, la función asigna un nivel de dificultad a `n_pregunta` utilizando las siguientes reglas:  
    - Si `p_level` es 2:  
        - 'básico' para las preguntas 1 y 2.  
        - 'intermedio' para las preguntas 3 y 4.  
        - 'avanzado' para las preguntas 5 y 6.  
    - Si `p_level` es 3:  
        - 'básico' para las preguntas 1, 2 y 3.  
        - 'intermedio' para las preguntas 4, 5 y 6.  
        - 'avanzado' para las preguntas 7, 8 y 9.  

    :param n_pregunta: int, el número de pregunta actual (puede ser positivo).  
    :param p_level: int, el máximo nivel de dificultad permitido (2 o 3).  
    :return: str, el nivel de dificultad como una cadena ('basico', 'intermedio', 'avanzado').  
    
    Ejemplos:  
    >>> choose_level(2, 2)  # Devuelve 'basico'  
    >>> choose_level(4, 2)  # Devuelve 'intermedio'  
    >>> choose_level(5, 2)  # Devuelve 'avanzado'  
    >>> choose_level(3, 3)  # Devuelve 'basico'  
    >>> choose_level(6, 3)  # Devuelve 'intermedio'  
    >>> choose_level(8, 3)  # Devuelve 'avanzado'  
    """   
    if p_level == 2:
        if 1 <= n_pregunta <= 2:
            level = "basico"
        elif 3 <= n_pregunta <= 4:
            level = "intermedio"
        elif 5 <= n_pregunta <= 6:
            level = "avanzado"

    elif p_level == 3:
        if 1 <= n_pregunta <= 3:
            level = "basico"
        elif 4 <= n_pregunta <= 6:
            level = "intermedio"
        elif 7 <= n_pregunta <= 9:
            level = "avanzado"

    return level


if __name__ == '__main__':
    # verificar resultados
    print(choose_level(2, 2))  # básicas
    print(choose_level(3, 2))  # intermedias
    print(choose_level(7, 2))  # avanzadas
    print(choose_level(4, 3))  # intermedias
