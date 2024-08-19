
def validate(opciones, eleccion):
    """Se crea funcion para crear ciclo while hasta que se ingrese eleccion valida
    El ciclo se seguira repitiendo hasta que el usuario ingrese una opcion valida (numeros o letras)
    Argumentos:
    opciones (lista): son las opciones validad entregadas por el programa
    eleccion (string): Opcion indicada por el usuario
    """
    while eleccion not in opciones:
        print(
            f"Opción no valida, ingrese una de las opciones validas: {opciones}")

        eleccion = input("Ingrese una opcion valida: ").lower()
    return eleccion


if __name__ == '__main__':

    eleccion = input('Ingresa una Opción: ').lower()

    letras = ['a', 'b', 'c', 'd']
    numeros = ['0', '1']

    opciones = letras  # se puede cambiar por la variable numeros

    eleccion_correcta = validate(opciones, eleccion)

    print(f"La opcion {eleccion_correcta} es una opcion valida.")
