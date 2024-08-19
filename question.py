import preguntas as p
import random
from shuffle import shuffle_alt

# Opciones dadas para escoger.
###############################################
opciones = {'basicas': ['pregunta_1', 'pregunta_2', 'pregunta_3'],
            'intermedias': ['pregunta_1', 'pregunta_2', 'pregunta_3'],
            'avanzadas': ['pregunta_1', 'pregunta_2', 'pregunta_3']}
###############################################

def choose_q(dificultad):
    # Escoger preguntas por dificultad
    preguntas = p.pool_preguntas[dificultad]

    # Usar opciones desde ambiente global
    global opciones

    # Escoger una pregunta al azar de las disponibles
    n_elegido = random.choice(opciones[dificultad])

    # Eliminarla del ambiente global para no escogerla de nuevo
    opciones[dificultad].remove(n_elegido)

    # Escoger enunciado y alternativas mezcladas
    pregunta = preguntas[n_elegido]
    alternativas = shuffle_alt(pregunta)

    return pregunta['enunciado'][0], alternativas

if __name__ == '__main__':
    # Ejemplo de uso
    enunciado, alternativas = choose_q('basicas')
    print(f'Enunciado: {enunciado}')
    print(f'Alternativas: {alternativas}')
