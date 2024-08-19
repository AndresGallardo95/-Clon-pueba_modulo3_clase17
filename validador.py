
def validate(opciones, eleccion):
    # Definir validación de eleccion
    ##########################################################################
    pass

    ##########################################################################
    return eleccion


if __name__ == '__main__':

    eleccion = input('Ingresa una Opción: ').lower()

    letras = ['a', 'b', 'c', 'd']
    numeros = ['0', '1']

    opciones = letras  # se puede cambiar por la variable numeros

    eleccion_correcta = validate(opciones, eleccion)

    print(f"La opcion {eleccion_correcta} es una opcion valida.")
