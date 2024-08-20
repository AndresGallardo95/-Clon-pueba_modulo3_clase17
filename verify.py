import preguntas as p


def verificar(alternativas, eleccion):
        """  
    Verifica si la elección del usuario es correcta comparándola con las alternativas dadas.  

    Esta función busca el índice de la elección del usuario en la lista de alternativas  
    y comprueba si la alternativa seleccionada es la correcta. Imprime un mensaje indicando  
    si la respuesta es correcta o incorrecta.  

    :param alternativas: list, una lista de alternativas donde cada alternativa es una tupla que contiene   
                        la opción (str) y un indicador de si es correcta (int, 1 para correcta, 0 para incorrecta).  
    :param eleccion: str, la alternativa elegida por el usuario ('a', 'b', 'c', 'd').  
    
    :return: bool, devuelve True si la elección es correcta, False en caso contrario.  

    Ejemplo:  
    >>> alternativas = [('a) Respuesta A', 0), ('b) Respuesta B', 1), ('c) Respuesta C', 0), ('d) Respuesta D', 0)]  
    >>> verificar(alternativas, 'b')  # Devuelve True e imprime 'Respuesta Correcta'  
    >>> verificar(alternativas, 'a')  # Devuelve False e imprime 'Respuesta Incorrecta'  
    """ 
    
    # Devuelve el índice de elección dada
    eleccion = ['a', 'b', 'c', 'd'].index(eleccion)
    
    # Verificar si la alternativa escogida es la correcta
    correcto = alternativas[eleccion][1] == 1
    
    # Imprimir resultado
    if correcto:
        print('Respuesta Correcta')
    else:
        print('Respuesta Incorrecta')
    
    return correcto



if __name__ == '__main__':
    from print_preguntas import print_pregunta
    
    # Siempre que se escoja la alternativa con alt_2 estará correcta, e incorrecta en cualquier otro caso
    pregunta = p.pool_preguntas['basicas']['pregunta_2']
    print_pregunta(pregunta['enunciado'],pregunta['alternativas'])
    respuesta = input('Escoja la alternativa correcta:\n> ').lower()
    verificar(pregunta['alternativas'], respuesta)








