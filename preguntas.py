preguntas_basicas = {
    'pregunta_1': {
        'enunciado': ['¿Cuál es el océano más grande del mundo?'],
        'alternativas': [
            ['Atlántico', 0], 
            ['Índico', 0], 
            ['Ártico', 0], 
            ['Pacífico', 1]
        ]
    },
    'pregunta_2': {
        'enunciado': ['¿En qué año llegó el hombre a la Luna?'],
        'alternativas': [
            ['1965', 0], 
            ['1969', 1], 
            ['1972', 0], 
            ['1980', 0]
        ]
    },
    'pregunta_3': {
        'enunciado': ['¿Cuál es la capital de Francia?'],
        'alternativas': [
            ['Berlín', 0], 
            ['Madrid', 0], 
            ['París', 1], 
            ['Roma', 0]
        ]
    }
}

preguntas_intermedias = {
    'pregunta_1': {
        'enunciado': ['¿Cuál es la fórmula química del agua?'],
        'alternativas': [
            ['H2O', 1], 
            ['CO2', 0], 
            ['O2', 0], 
            ['N2', 0]
        ]
    },
    'pregunta_2': {
        'enunciado': ['¿Quién escribió "Don Quijote de la Mancha"?'],
        'alternativas': [
            ['Miguel de Cervantes', 1], 
            ['Gabriel García Márquez', 0], 
            ['Jorge Luis Borges', 0], 
            ['Pablo Neruda', 0]
        ]
    },
    'pregunta_3': {
        'enunciado': ['¿Cuál es el metal más abundante en la Tierra?'],
        'alternativas': [
            ['Hierro', 1], 
            ['Cobre', 0], 
            ['Oro', 0], 
            ['Plata', 0]
        ]
    }
}

preguntas_avanzadas = {
    'pregunta_1': {
        'enunciado': ['¿Cuál es la distancia promedio entre la Tierra y la Luna?'],
        'alternativas': [
            ['384,400 km', 1], 
            ['150,000 km', 0], 
            ['1,000,000 km', 0], 
            ['300,000 km', 0]
        ]
    },
    'pregunta_2': {
        'enunciado': ['¿Qué científico desarrolló la teoría de la relatividad?'],
        'alternativas': [
            ['Albert Einstein', 1], 
            ['Isaac Newton', 0], 
            ['Galileo Galilei', 0], 
            ['Nikola Tesla', 0]
        ]
    },
    'pregunta_3': {
        'enunciado': ['¿Cuál es el idioma oficial en Brasil?'],
        'alternativas': [
            ['Portugués', 1], 
            ['Español', 0], 
            ['Inglés', 0], 
            ['Francés', 0]
        ]
    }
}

pool_preguntas = {
    'basicas': preguntas_basicas,
    'intermedias': preguntas_intermedias,
    'avanzadas': preguntas_avanzadas
}
