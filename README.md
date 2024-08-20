# APP ADL desarrolladores // Fundamentos de programación en Python

ADL Desarrolladores es una entidad dedicada a desarrollar apps entretenidas.
Se desarrolla una App en Python que permite jugar una trivia interactiva. Esta App tendrá preguntas con 3 niveles de dificultad:

● Básica
● Intermedia
● Avanzada

El jugador define el número de preguntas a responder correspondientes a cada nivel de dificultad, y gana al responder todas las preguntas correctamente. Las preguntas deben aparecer en un orden aleatorio, y además cada vez que alguien ejecute la app las alternativas deben ser cambiadas de orden para evitar que alguien encuentre algún patrón de resolución.

Ya que el programa es complejo se ha generado un backlog con tareas muy específicas, las cuales son desarrolladas paso a paso antes de ensamblar la app final.
Todas las subtareas consistirán en la creación de un script en Python, la que contendrá las especificaciones de una funcionalidad.

## 01 - validador.py

Se crea un programa llamado validador.py el cual permite validar si un valor se encuentra incluido en un conjunto de opciones.

En caso de que no se ingrese una opción dentro del conjunto, la aplicación muestra un mensaje de error y
solicita un nuevo valor hasta que se ingrese uno válido.

## 02 - level.py

El programa llamado level.py permite escoger el nivel de dificultad de la pregunta a realizar. Este programa debe solicitar número de la pregunta, y la cantidad de preguntas por nivel que puede ser 1, 2 o 3.

## 03 - shuffle.py

El programa llamado shuffle.py toma preguntas desde el archivo preguntas.py (con un nivel y una pregunta definida) y mezcla las alternativas para no darle un patron especifico.

## 04 - question.py

El programa llamado question.py permite escoger una pregunta que no se haya hecho durante la ejecución del programa dependiendo del nivel de dificultad.

Toma las preguntas del archivo preguntas.py de acuerdo a la dificultad escogida. Escoge una pregunta de las opciones disponibles y elimina dicha opción para no volverla a escoger.

## 05 - print_preguntas.py

El programa llamado print_preguntas.py, permite mostrar en la app las preguntas de acuerdo a un formato
El formato a utilizar es imprimir el enunciado,seguido de un salto de línea. Luego cada alternativa irá acompañada una letra asociada, una por cada línea de la siguiente manera:

○ A. Alternativa 1
○ B. Alternativa 2
○ C. Alternativa 3
○ D. Alternativa 4

## 06- verify.py

El programa llamado verify.py, cuya función es verificar si la respuesta entregada por el usuario es correcta.
En el caso que la respuesta sea correcta se imprime en pantalla 'Respuesta Correcta' y retornar sólo el valor True, en caso contrario se imprime en pantalla
'Respuesta Incorrecta' y retornar sólo el valor False.

## 07 - main.py

El programa main.py corresponde a la union de los programas anteriores para desarrollar el funcionamiento completo de la app solicitada por el cliente, consiste en el juego de trivias con 3 niveles de dificultad (basico, intermedio y avanzado).

## Prerrequisitos o Dependencias

Sistema Operativo Windows, Linux, MacOS
Lenguaje de programación Python 3.12

## Instalación del Proyecto

Clonar el repositorio:

```bash
# git@github.com:vanemn/prueba_modulo3_clase17.git
```

Ingresar a la carpeta del proyecto:

```bash
# prueba_modulo3_clase17
```

Autor

- [Vanessa Morales](https://github.com/vanemn)
- [Benjamín Pardo](https://github.com/bpardo02)
- [Nicole Pinilla](https://github.com/Npinilla19)
