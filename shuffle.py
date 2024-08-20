import preguntas as p
import random

def shuffle_alt(pregunta):
        """  
    Mezcla aleatoriamente las alternativas de una pregunta dada.  

    Esta función toma una pregunta en forma de diccionario,  
    extrae sus alternativas y mezcla su orden de manera aleatoria.  
    La lista original de alternativas se modifica en su lugar.  

    Parámetros:  
    ----------  
    pregunta : dict  
        Un diccionario que representa una pregunta. Debe contener una clave  
        'alternativas', que se espera sea una lista de listas,  
        donde cada lista interna representa una alternativa como [opción, valor].  

    Retorna:  
    -------  
    list  
        La lista de alternativas mezcladas de la pregunta de entrada.  
    """  
    
    alternativas = (pregunta['alternativas'])
    random.shuffle(alternativas)
    return pregunta['alternativas']

if __name__ == '__main__':
    # si se ejecuta el  programa varias veces las alternativas debieran aparecer en distinto orden
    print(shuffle_alt(p.pool_preguntas['basicas']['pregunta_1'])) 
    # a modo de ejemplo
    # [['alt_1', 0], ['alt_3', 0], ['alt_2', 1], ['alt_4', 0]]
