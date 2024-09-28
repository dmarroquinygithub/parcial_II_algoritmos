# Función que calcula la superficie de un rectángulo
def superficie_rectangulo(lado1, lado2):
    return lado1 * lado2

# Bloque principal del programa
def comparar_superficies():
    # Cargar los valores de los lados del primer rectángulo
    lado1_rect1 = float(input("Ingrese el lado 1 del primer rectángulo: "))
    lado2_rect1 = float(input("Ingrese el lado 2 del primer rectángulo: "))

    # Cargar los valores de los lados del segundo rectángulo
    lado1_rect2 = float(input("Ingrese el lado 1 del segundo rectángulo: "))
    lado2_rect2 = float(input("Ingrese el lado 2 del segundo rectángulo: "))

    # Calcular las superficies
    superficie1 = superficie_rectangulo(lado1_rect1, lado2_rect1)
    superficie2 = superficie_rectangulo(lado1_rect2, lado2_rect2)

    # Mostrar cuál de los dos tiene una superficie mayor
    if superficie1 > superficie2:
        print("El primer rectángulo tiene una superficie mayor.")
    elif superficie2 > superficie1:
        print("El segundo rectángulo tiene una superficie mayor.")
    else:
        print("Ambos rectángulos tienen la misma superficie.")

# Llamar al bloque principal
comparar_superficies()
