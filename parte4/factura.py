from typing import List
from linea_factura import LineaFactura
from producto import Producto
from descuento import Descuento


class Factura:
    """
    GRASP Creator: Factura contiene y administra las instancias de LineaFactura,
    por lo tanto es la responsable de crearlas.

    El método agregar_linea() recibe los datos necesarios, instancia una nueva
    LineaFactura y la incorpora a su colección interna.
    """

    def __init__(self, numero: str, cliente: str):
        self.numero = numero
        self.cliente = cliente
        self.lineas: List[LineaFactura] = []

    def agregar_linea(self, producto: Producto, cantidad: int, descuento: Descuento = None):
        """Creator: crea e incorpora una nueva LineaFactura a la factura."""
        nueva_linea = LineaFactura(producto, cantidad, descuento)
        self.lineas.append(nueva_linea)

    def calcular_total_bruto(self) -> float:
        return sum(linea.calcular_subtotal_bruto() for linea in self.lineas)

    def calcular_total_descuentos(self) -> float:
        return sum(linea.calcular_monto_descuento() for linea in self.lineas)

    def calcular_total_neto(self) -> float:
        return sum(linea.calcular_subtotal_neto() for linea in self.lineas)
