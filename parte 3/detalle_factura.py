from producto import Producto
from descuentos import Descuento, SinDescuento


class DetalleFactura:
    """
    Representa una línea o ítem dentro de la factura.
    Recibe dinámicamente una estrategia de descuento (Polimorfismo).
    """
    
    def __init__(self, producto: Producto, cantidad: int, descuento: Descuento = None):
        self.producto = producto
        self.cantidad = cantidad
        # Si no se especifica un descuento, se usa SinDescuento por defecto (Null Object Pattern)
        self.descuento = descuento if descuento is not None else SinDescuento()

    def calcular_subtotal_bruto(self) -> float:
        return self.producto.precio_unitario * self.cantidad

    def calcular_monto_descuento(self) -> float:
        subtotal_bruto = self.calcular_subtotal_bruto()
        # DELEGACIÓN POLIMÓRFICA: Sin condicionales (if/else) según el tipo de descuento
        return self.descuento.calcular_descuento(
            subtotal=subtotal_bruto,
            cantidad=self.cantidad,
            categoria=self.producto.categoria
        )

    def calcular_subtotal_neto(self) -> float:
        return self.calcular_subtotal_bruto() - self.calcular_monto_descuento()
