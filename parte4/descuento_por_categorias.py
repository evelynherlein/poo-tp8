from descuento import Descuento


class DescuentoPorCategorias(Descuento):
    """
    Implementación concreta: Aplica descuento si la categoría del producto
    coincide con la categoría promocionada.
    Ejemplo: 10% de descuento para la categoría 'Electrónica'.
    """

    def __init__(self, categoria_promocionada: str, porcentaje: float):
        self.categoria_promocionada = categoria_promocionada.lower()
        self.porcentaje = porcentaje / 100.0

    def calcular_descuento(self, subtotal: float, cantidad: int = 1, categoria: str = "") -> float:
        if categoria.lower() == self.categoria_promocionada:
            return subtotal * self.porcentaje
        return 0.0
