from tablero import MatrizBoop


def juego():
    print("Bienvenido a Boop")
    iniciar = input("Para nuevo juego pulse 1: ")

    if iniciar == "1":
        tamano_tablero = int(input("* Escoja el tamaño del tablero "))
        tablero = MatrizBoop(tamano_tablero)
        tablero.mostrar_matriz()


        while True:
            try:
                coordenadas = input("Ingrese las coordenadas: ")


                fila, columna = map(int, coordenadas.split(","))

                if not fila > tablero.size and not columna > tablero.size:
                    tablero.colocar_gato(fila, columna)
                    tablero.mostrar_matriz()

                    if tablero.verificar_condicion() == True:
                        print("Ganaste!")
                        break

            except (ValueError):
                print("Debe poner las coordenadas, x,y ")




def main():
    while True:
        juego()
        break


if __name__ == "__main__":
    main()
