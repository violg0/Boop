from gato import Gato
from typing import Optional


class NodoMatriz:
    def __init__(self, gato: Optional[Gato] = None):
        self.gato: Optional[Gato] = gato
        self.arriba: Optional['NodoMatriz'] = None
        self.abajo: Optional['NodoMatriz'] = None
        self.izquierda: Optional['NodoMatriz'] = None
        self.derecha: Optional['NodoMatriz'] = None
        self.diagonal_izq_sup: Optional['NodoMatriz'] = None
        self.diagonal_der_sup: Optional['NodoMatriz'] = None
        self.diagonal_izq_inf: Optional['NodoMatriz'] = None
        self.diagonal_der_inf: Optional['NodoMatriz'] = None

    def __repr__(self):
        return f"{self.gato}<->{self.derecha}"

    def agregar_gato(self):
        self.gato = Gato(" 🐱 ")

    def mover_gato(self):
        self.gato = None


class DoubleLinkedList:
    def __init__(self):
        self.head: Optional[NodoMatriz] = None
        self.tail: Optional[NodoMatriz] = None
        self.size: int = 0

    def __repr__(self):
        return f"{self.head}"


    def append(self, value: Optional[Gato]) -> NodoMatriz:
        new_node = NodoMatriz(value)
        self.size += 1
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            old_tail = self.tail
            self.tail.derecha = new_node
            self.tail = new_node
            self.tail.izquierda = old_tail

        return new_node

    def colocar_en_un_indice(self, index: int) -> Optional[NodoMatriz]:
        if index < 0 or index >= self.size:
            raise IndexError

        current_node = self.head
        for i in range(index):
            current_node = current_node.derecha
        if current_node.gato is not None:
            return False

        current_node.agregar_gato()
        return current_node

    def buscar_indice(self, index: int) -> NodoMatriz:
        if index < 0 or index >= self.size:
            raise IndexError

        current_node = self.head
        for i in range(index):
            current_node = current_node.derecha

        return current_node
