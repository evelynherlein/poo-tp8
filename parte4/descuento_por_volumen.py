from descuento import Descuento


class DescuentoPorVolumen(Descuento):
    """
    Implementación concreta: Aplica descuento si la cantidad supera un umbral.
    Ejemplo: 15% de descuento si se compran 5 o más unidades.
    """

    def __init__(self, umbral_cantidad: int, porcentaje: float):
        self.umbral_cantidad = umbral_cantidad
        self.porcentaje = porcentaje / 100.0

    def calcular_descuento(self, subtotal: float, cantidad: int = 1, categoria: str = "") -> float:
        if cantidad >= self.umbral_cantidad:
            return subtotal * self.porcentaje
        return 0.0
