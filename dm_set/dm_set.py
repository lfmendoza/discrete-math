from .node import Node

class DMSet:
    """
    Clase que representa un conjunto utilizando una estructura de datos basada en un set.
    """

    def __init__(self):
        """
        Inicializa un conjunto vacío para almacenar los elementos.
        """
        self.elements = set()

    def add(self, value):
        """
        Añade un valor al conjunto si no existe ya en él.

        :param value: El valor a añadir al conjunto.
        :type value: any
        """
        self.elements.add(value)

    def remove(self, value):
        """
        Elimina un valor del conjunto si existe.

        :param value: El valor a eliminar del conjunto.
        :type value: any
        """
        self.elements.discard(value)  # `discard` no arroja un error si el valor no está presente

    def contains(self, value):
        """
        Verifica si un valor está en el conjunto.

        :param value: El valor a verificar en el conjunto.
        :type value: any
        :return: True si el valor existe en el conjunto, False en caso contrario.
        :rtype: bool
        """
        return value in self.elements

    def union(self, other):
        """
        Retorna un nuevo conjunto que es la unión del conjunto actual y otro conjunto.

        :param other: Otro conjunto con el que realizar la unión.
        :type other: DMSet
        :return: Un nuevo conjunto que contiene todos los elementos únicos de ambos conjuntos.
        :rtype: DMSet
        """
        result = DMSet()
        result.elements = self.elements.union(other.elements)
        return result

    def intersection(self, other):
        """
        Retorna un nuevo conjunto que es la intersección del conjunto actual y otro conjunto.

        :param other: Otro conjunto con el que realizar la intersección.
        :type other: DMSet
        :return: Un nuevo conjunto que contiene solo los elementos presentes en ambos conjuntos.
        :rtype: DMSet
        """
        result = DMSet()
        result.elements = self.elements.intersection(other.elements)
        return result

    def complement(self, universal_set):
        """
        Retorna un nuevo conjunto que es el complemento del conjunto actual con respecto a un conjunto universal.

        :param universal_set: El conjunto universal con el que comparar.
        :type universal_set: DMSet
        :return: Un nuevo conjunto que contiene elementos en el conjunto universal pero no en el conjunto actual.
        :rtype: DMSet
        """
        result = DMSet()
        result.elements = universal_set.elements.difference(self.elements)
        return result

    def difference(self, other):
        """
        Retorna un nuevo conjunto que es la diferencia entre el conjunto actual y otro conjunto.

        :param other: Otro conjunto que se va a restar del conjunto actual.
        :type other: DMSet
        :return: Un nuevo conjunto que contiene elementos en el conjunto actual pero no en el otro conjunto.
        :rtype: DMSet
        """
        result = DMSet()
        result.elements = self.elements.difference(other.elements)
        return result

    def symmetric_difference(self, other):
        """
        Retorna un nuevo conjunto que es la diferencia simétrica entre el conjunto actual y otro conjunto.

        :param other: Otro conjunto con el que realizar la diferencia simétrica.
        :type other: DMSet
        :return: Un nuevo conjunto que contiene los elementos que están en cualquiera de los conjuntos pero no en ambos.
        :rtype: DMSet
        """
        return self.union(other).difference(self.intersection(other))

    def __str__(self):
        """
        Retorna una representación en cadena del conjunto.

        :return: Una cadena en formato "{element1, element2, ...}" que representa el conjunto.
        :rtype: str
        """
        return "{" + ", ".join(map(str, sorted(self.elements))) + "}"
