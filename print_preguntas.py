import preguntas as p

def print_pregunta(enunciado, alternativas):
    """
    Imprime el enunciado de una pregunta y sus alternativas con letras correspondientes.

    Args:
        enunciado (str): El texto del enunciado de la pregunta.
        alternativas (list): Una lista de tuplas, donde cada tupla contiene una alternativa 
                             como primer elemento y su estado (correcta o incorrecta) como segundo elemento.

    Example:
        enunciado = "¿Cuál es la capital de Francia?"
        alternativas = [("París", True), ("Londres", False), ("Madrid", False), ("Berlín", False)]
        
        print_pregunta(enunciado, alternativas)
        # Output:
        # ¿Cuál es la capital de Francia?
        #
        # A. París
        # B. Londres
        # C. Madrid
        # D. Berlín
    """
    
    print(f'{enunciado}\n')
    for i, (alt, _) in enumerate(alternativas):
        print(f'{chr(65+i)}. {alt}')

if __name__ == '__main__':
    # Las preguntas y alternativas deben mostrarse según lo indicado
    pregunta = p.pool_preguntas['basicas']['pregunta_1']
    print_pregunta(pregunta['enunciado'],pregunta['alternativas'])
    
    # Enunciado básico 1

    # A. alt_1
    # B. alt_2
    # C. alt_3
    # D. alt_4