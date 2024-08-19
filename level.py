def choose_level(n_pregunta, p_level):
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
