from abc import ABC, abstractmethod


class Descuento(ABC):
    """
    Clase Abstracta / Interfaz Descuento (Patrón GRASP Polimorfismo).
    Define el contrato para calcular el monto del descuento sobre una venta o ítem.
    """
    
    @abstractmethod
    def calcular_descuento(self, subtotal: float, cantidad: int = 1, categoria: str = "") -> float:
        """Calcula y retorna el valor en pesos del descuento a aplicar."""
        pass


class SinDescuento(Descuento):
    """Implementación concreta: No aplica ningún descuento."""
    
    def calcular_descuento(self, subtotal: float, cantidad: int = 1, categoria: str = "") -> float:
        return 0.0


class DescuentoPorVolumen(Descuento):
    """
    Implementación concreta: Aplica descuento si la cantidad supera un umbral determinado.
    Ejemplo: 15% de descuento si se compran 5 o más unidades.
    """
    
    def __init__(self, umbral_cantidad: int, porcentaje: float):
        self.umbral_cantidad = umbral_cantidad
        self.porcentaje = porcentaje / 100.0

    def calcular_descuento(self, subtotal: float, cantidad: int = 1, categoria: str = "") -> float:
        if cantidad >= self.umbral_cantidad:
            return subtotal * self.porcentaje
        return 0.0


class DescuentoPorCategoria(Descuento):
    """
    Implementación concreta: Aplica descuento si la categoría coincide con la promocionada.
    Ejemplo: 20% de descuento para productos de la categoría 'Electrónica'.
    """
    
    def __init__(self, categoria_promocionada: str, porcentaje: float):
        self.categoria_promocionada = categoria_promocionada.lower()
        self.porcentaje = porcentaje / 100.0

    def calcular_descuento(self, subtotal: float, cantidad: int = 1, categoria: str = "") -> float:
        if categoria.lower() == self.categoria_promocionada:
            return subtotal * self.porcentaje
        return 0.0


class DescuentoFijoPorcentaje(Descuento):
    """
    Implementación concreta: Aplica un porcentaje fijo de descuento incondicional.
    Ejemplo: Descuento del 10% por pago al contado o promoción especial.
    """
    
    def __init__(self, porcentaje: float):
        self.porcentaje = porcentaje / 100.0

    def calcular_descuento(self, subtotal: float, cantidad: int = 1, categoria: str = "") -> float:
        return subtotal * self.porcentaje
