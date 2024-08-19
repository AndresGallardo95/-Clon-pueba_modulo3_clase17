
def validate(opciones, eleccion):
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
