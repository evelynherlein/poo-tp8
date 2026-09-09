from abc import ABC, abstractmethod


class Descuento(ABC):
    """
    Clase Abstracta / Interfaz Descuento (GRASP Polimorfismo).
    Define el contrato que todas las estrategias de descuento deben cumplir.
    """

    @abstractmethod
    def calcular_descuento(self, subtotal: float, cantidad: int = 1, categoria: str = "") -> float:
        """Calcula y retorna el valor en pesos del descuento a aplicar."""
        pass
