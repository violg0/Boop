import unittest
from tablero import MatrizBoop

class TestMatrizBoop(unittest.TestCase):

    def setUp(self):

        self.tamano_tablero = 3
        self.tablero = MatrizBoop(self.tamano_tablero)

    def test_crear_matriz(self):
        self.assertEqual(self.tablero.size, self.tamano_tablero)
        self.assertIsNotNone(self.tablero.matriz)

    def test_colocar_gato_en_casilla_vacia(self):
        fila, columna = 2, 2
        self.tablero.colocar_gato(fila, columna)

        fila_actual = self.tablero.matriz.head
        for i in range(fila-1):
            fila_actual = fila_actual.derecha

        casilla_gato = fila_actual.gato.buscar_indice(columna-1)

        with self.assertRaises(ValueError):
            self.tablero.colocar_gato(fila, columna)



    def test_colocar_gato_en_una_posicion_ocupada(self):
        fila, columna = 1, 1
        self.tablero.colocar_gato(fila, columna)

        fila_actual = self.tablero.matriz.head
        for i in range(fila-1):
            fila_actual = fila_actual.derecha

        casilla_gato = fila_actual.gato.buscar_indice(columna-1)

        with self.assertRaises(Exception):
            self.tablero.colocar_gato(fila, columna)


    def test_verificar_condicion_ganar(self):
        self.tablero.colocar_gato(1, 1)
        self.tablero.colocar_gato(3, 1)

        self.tablero.colocar_gato(2, 2)

        self.assertTrue(self.tablero.verificar_condicion())

    def test_mover_gatos_adyacentes(self):

        fila, columna = 1, 1
        self.tablero.colocar_gato(fila, columna)

        self.tablero.colocar_gato(1, 2)
        self.tablero.colocar_gato(2, 1)

        casilla_gato_adyacente1 = self.tablero.matriz.head.gato.buscar_indice(1)
        casilla_gato_adyacente2 = self.tablero.matriz.head.derecha.gato.head


        self.assertIsNone(casilla_gato_adyacente1.gato)
        self.assertIsNotNone(casilla_gato_adyacente2.gato)


    def test_matriz_con_gatos(self):
        self.tablero.matriz_con_gatos()

        cantidad_gatos = 0
        fila_actual = self.tablero.matriz.head

        for i in range(self.tablero.size):
            nodo_actual = fila_actual.gato.head

            while nodo_actual is not None:
                if nodo_actual.gato is not None:
                    cantidad_gatos += 1
                nodo_actual = nodo_actual.derecha

            fila_actual = fila_actual.derecha

        self.assertGreater(cantidad_gatos, 0)

if __name__ == "__main__":
    unittest.main()
