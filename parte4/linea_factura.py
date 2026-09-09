from producto import Producto
from descuento import Descuento


class LineaFactura:
    """
    Information Expert: conoce el producto, la cantidad y la estrategia de descuento.
    Por lo tanto, es responsable de calcular su propio subtotal, descuento y total neto.

    Es instanciada por Factura (GRASP Creator), ya que Factura contiene
    y administra sus líneas.
    """

    def __init__(self, producto: Producto, cantidad: int, descuento: Descuento = None):
        self.producto = producto
        self.cantidad = cantidad
        self.descuento = descuento

    def calcular_subtotal_bruto(self) -> float:
        return self.producto.precio_unitario * self.cantidad

    def calcular_monto_descuento(self) -> float:
        if self.descuento is None:
            return 0.0
        # DELEGACIÓN POLIMÓRFICA: sin if/else según el tipo de descuento
        return self.descuento.calcular_descuento(
            subtotal=self.calcular_subtotal_bruto(),
            cantidad=self.cantidad,
            categoria=self.producto.categoria
        )

    def calcular_subtotal_neto(self) -> float:
        return self.calcular_subtotal_bruto() - self.calcular_monto_descuento()
