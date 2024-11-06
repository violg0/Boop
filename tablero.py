from ListaDoblementeEnlazada import DoubleLinkedList
from typing import Optional

import random


class MatrizBoop:
    def __init__(self, tamano: int) -> None:
        self.size:int = tamano
        self.matriz: DoubleLinkedList = DoubleLinkedList()
        self.crear_matriz()
        self.matriz_con_gatos()

    def crear_matriz(self) -> None:
        for i in range(self.size):
            fila = DoubleLinkedList()

            for j in range(self.size):
                nuevo_nodo = fila.append(None)


                if i > 0:
                    fila_arriba = self.matriz.head

                    for _ in range(i - 1):
                        fila_arriba = fila_arriba.derecha

                    nodo_arriba = fila_arriba.gato.head

                    for _ in range(j):
                        nodo_arriba = nodo_arriba.derecha

                    nuevo_nodo.arriba = nodo_arriba
                    nodo_arriba.abajo = nuevo_nodo

                    if j > 0:
                        nuevo_nodo.diagonal_izq_sup = nodo_arriba.izquierda
                        nodo_arriba.izquierda.diagonal_der_inf = nuevo_nodo

                    if j < self.size-1:
                        nuevo_nodo.diagonal_der_sup = nodo_arriba.derecha
                        nodo_arriba.derecha.diagonal_izq_inf = nuevo_nodo

            self.matriz.append(fila)

    def __str__(self)-> str:
        string_matriz = []
        current_fila = self.matriz.head

        while current_fila is not None:
            current_node = current_fila.gato.head
            str_fila = []
            while current_node is not None:
                if current_node.gato is not None:
                    str_fila.append(str(current_node.gato))
                else:
                    str_fila.append(str(" . "))
                current_node = current_node.derecha

            string_matriz.append("  ".join(str_fila))
            current_fila = current_fila.derecha
        return "\n".join(string_matriz)

    def matriz_con_gatos(self) -> Optional[DoubleLinkedList]:
        n = random.randint(1, self.size-1)
        gatos_colocados = 0

        for _ in range(n):
            while gatos_colocados < n:
                fila = random.randint(1, self.size-1)
                columna = random.randint(1, self.size-1)

                current_fila = self.matriz.head

                for i in range(fila):
                    current_fila = current_fila.derecha
                current_node = current_fila.gato.head

                for j in range(columna):
                    current_node = current_node.derecha

                    if j == columna-1:
                        if current_node.gato is None:
                            current_node.agregar_gato()
                            gatos_colocados += 1
                        else:
                            if current_node.derecha:
                                current_node.derecha.agregar_gato()
                                gatos_colocados += 1
                break
        return self.matriz




    def colocar_gato(self, fila: int, columna: int)-> None:
        fila_actual = self.matriz.head
        for i in range(fila-1):
            fila_actual = fila_actual.derecha

        casilla_gato = fila_actual.gato.buscar_indice(columna-1)

        if casilla_gato.gato is not None:
            coordenadas = input(f"ya hay un gato ahi, en {fila, columna} selecciona otra casilla: ")
            fila, columna = map(int, coordenadas.split(","))
            self.colocar_gato(fila, columna)

        fila_actual.gato.colocar_en_un_indice(columna-1)

        self.mover_adyacentes(fila, columna)


    def mover_adyacentes(self, fila: int, columna: int)-> None:

        fila_actual = self.matriz.head
        for i in range(fila-1):
            fila_actual = fila_actual.derecha

        nodo_actual = fila_actual.gato.buscar_indice(columna-1)

        #try:
            #if nodo_actual.arriba and nodo_actual.arriba.gato is not None:
                #nodo_actual.arriba.mover_gato()

                #if nodo_actual.arriba.arriba:
                    #if nodo_actual.arriba.arriba.gato is not None:
                        #nodo_actual.arriba.agregar_gato()
                    #else:
                        #nodo_actual.arriba.arriba.agregar_gato()

        #except AttributeError:
            #pass


        #try:
         #   if nodo_actual.abajo and nodo_actual.abajo.gato is not None:
          #      nodo_actual.abajo.mover_gato()

            #    if nodo_actual.abajo.abajo:
             #       if nodo_actual.abajo.abajo.gato is not None:
              #          nodo_actual.abajo.agregar_gato()
               #     else:
                #        nodo_actual.abajo.abajo.agregar_gato()
       # except AttributeError:
        #    pass

        #try:
         #   if nodo_actual.izquierda and nodo_actual.izquierda.gato is not None:
          #      nodo_actual.izquierda.mover_gato()

           #     if nodo_actual.izquierda.izquierda:
            #        if nodo_actual.izquierda.izquierda.gato is not None:
                 #       nodo_actual.izquierda.agregar_gato()
                  #  else:
                   #     nodo_actual.izquierda.izquierda.agregar_gato()

      #  except AttributeError:
        #    pass

       # try:
        #    if nodo_actual.derecha and nodo_actual.derecha.gato is not None:
           #     nodo_actual.derecha.mover_gato()

            #    if nodo_actual.derecha.derecha:
             #       if nodo_actual.derecha.derecha.gato is not None:
              #          nodo_actual.derecha.agregar_gato()
                  #  else:
                    #    nodo_actual.derecha.derecha.agregar_gato()
        #except AttributeError:
         #   pass

        try:
            if nodo_actual.diagonal_izq_sup and nodo_actual.diagonal_izq_sup.gato is not None:
                nodo_actual.diagonal_izq_sup.mover_gato()

                if nodo_actual.diagonal_izq_sup.arriba:
                    if nodo_actual.diagonal_izq_sup.diagonal_izq_sup.gato is not None:
                        nodo_actual.diagonal_izq_sup.agregar_gato()
                    else:
                        nodo_actual.diagonal_izq_sup.diagonal_izq_sup.agregar_gato()
        except AttributeError:
            pass

        try:
            if nodo_actual.diagonal_der_sup and nodo_actual.diagonal_der_sup.gato is not None:
                nodo_actual.diagonal_der_sup.mover_gato()

                if nodo_actual.diagonal_der_sup.diagonal_der_sup:
                    if nodo_actual.diagonal_der_sup.diagonal_der_sup.gato is not None:
                        nodo_actual.diagonal_der_sup.agregar_gato()
                    else:
                        nodo_actual.diagonal_der_sup.diagonal_der_sup.agregar_gato()
        except AttributeError:
            pass

        try:
            if nodo_actual.diagonal_izq_inf and nodo_actual.diagonal_izq_inf.gato is not None:
                nodo_actual.diagonal_izq_inf.mover_gato()

                if nodo_actual.diagonal_izq_inf.diagonal_izq_inf:
                    if nodo_actual.diagonal_izq_inf.diagonal_izq_inf.gato is not None:
                        nodo_actual.diagonal_izq_inf.agregar_gato()
                    else:
                        nodo_actual.diagonal_izq_inf.diagonal_izq_inf.agregar_gato()
        except AttributeError:
            pass

        try:
            if nodo_actual.diagonal_der_inf and nodo_actual.diagonal_der_inf.gato is not None:
                nodo_actual.diagonal_der_inf.mover_gato()

                if nodo_actual.diagonal_der_inf.diagonal_der_inf:
                    if nodo_actual.diagonal_der_inf.diagonal_der_inf.gato is not None:
                        nodo_actual.diagonal_der_inf.agregar_gato()
                    else:
                        nodo_actual.diagonal_der_inf.diagonal_der_inf.agregar_gato()
        except AttributeError:
            pass


        self.mover_filas_columnas(fila, columna, fila_actual)

    def mover_filas_columnas(self, fila, columna, fila_actual) -> None:
        nodo_actual = fila_actual.gato.buscar_indice(columna-1)
        print("nodo actual", columna-1)
        i = 0
        while nodo_actual is not None:
            if nodo_actual.derecha and nodo_actual.derecha.gato is not None:
                nodo_actual.derecha.mover_gato()

                if nodo_actual.derecha.derecha:
                    if nodo_actual.derecha.derecha.gato is not None:
                        nodo_actual.derecha.agregar_gato()
                        nodo_actual = nodo_actual.derecha
                    else:
                        print("se movio el gato", i)
                        nodo_actual.derecha.derecha.agregar_gato()
                        nodo_actual = nodo_actual.derecha.derecha
            else:
                nodo_actual = nodo_actual.derecha

            i+=1

        nodo_actual = fila_actual.gato.buscar_indice(columna-1)



        while nodo_actual is not None:
            if nodo_actual.izquierda and nodo_actual.izquierda.gato is not None:
                nodo_actual.izquierda.mover_gato()

                if nodo_actual.izquierda.izquierda:
                    if nodo_actual.izquierda.izquierda.gato is not None:
                        nodo_actual.izquierda.agregar_gato()
                        nodo_actual = nodo_actual.izquierda
                    else:
                        nodo_actual.izquierda.izquierda.agregar_gato()
                        nodo_actual = nodo_actual.izquierda.izquierda
            else:
                nodo_actual = nodo_actual.izquierda

            i += 1

        nodo_actual = fila_actual.gato.buscar_indice(columna-1)

        while nodo_actual is not None:
            if nodo_actual.abajo and nodo_actual.abajo.gato is not None:
                nodo_actual.abajo.mover_gato()

                if nodo_actual.abajo.abajo:
                    if nodo_actual.abajo.abajo.gato is not None:
                        nodo_actual.abajo.agregar_gato()
                        nodo_actual = nodo_actual.abajo
                    else:
                        nodo_actual.abajo.abajo.agregar_gato()
                        nodo_actual = nodo_actual.abajo.abajo
                else:
                    print("no hay abajo")
                    break
            else:
                nodo_actual = nodo_actual.abajo


        nodo_actual = fila_actual.gato.buscar_indice(columna-1)

        while nodo_actual is not None:
            if nodo_actual.arriba and nodo_actual.arriba.gato is not None:
                nodo_actual.arriba.mover_gato()

                if nodo_actual.arriba.arriba:
                    if nodo_actual.arriba.arriba.gato is not None:
                        nodo_actual.arriba.agregar_gato()
                        nodo_actual = nodo_actual.arriba
                    else:
                        nodo_actual.arriba.arriba.agregar_gato()
                        nodo_actual = nodo_actual.arriba.arriba
            else:
                nodo_actual = nodo_actual.arriba

            i += 1




    def verificar_condicion(self)-> bool:
        cantidad_de_gatos = 0
        fila_actual = self.matriz.head

        while fila_actual is not None:
            nodo_actual = fila_actual.gato.head
            while nodo_actual is not None:
                if nodo_actual.gato is not None:
                    cantidad_de_gatos += 1
                nodo_actual = nodo_actual.derecha
            fila_actual = fila_actual.derecha

        if cantidad_de_gatos == 1:
            return True
        return False


    def mostrar_matriz(self)-> None:
        print(self)











