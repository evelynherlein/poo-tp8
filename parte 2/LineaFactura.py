from Producto import Producto


class LineaFactura:
    """Information Expert: conoce cantidad, producto y tasa.
    Por lo tanto calcula su propio neto, descuento e IVA."""

    def __init__(self, producto: Producto, cantidad: float):
        self.producto = producto
        self.cantidad = cantidad

    def calcular_neto_bruto(self):
        return self.cantidad * self.producto.precio_base

    def calcular_neto_con_descuento(self, porcentaje_descuento: float):
        neto_bruto = self.calcular_neto_bruto()
        return neto_bruto * (1 - porcentaje_descuento)

    def calcular_iva(self, porcentaje_descuento: float):
        # El IVA se calcula sobre el neto YA descontado, línea por línea
        neto_descontado = self.calcular_neto_con_descuento(porcentaje_descuento)
        return neto_descontado * self.producto.porcentaje_iva

    def calcular_total(self, porcentaje_descuento: float):
        neto_descontado = self.calcular_neto_con_descuento(porcentaje_descuento)
        return neto_descontado + self.calcular_iva(porcentaje_descuento)
