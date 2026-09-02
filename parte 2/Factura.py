from LineaFactura import LineaFactura


class Factura:
    """Coordina sus líneas y acumula totales. No calcula el detalle
    matemático de cada línea: eso es responsabilidad de LineaFactura."""

    def __init__(self, tipo_comprobante: str, porcentaje_descuento: float, lineas: list[LineaFactura]):
        self.tipo_comprobante = tipo_comprobante
        self.porcentaje_descuento = porcentaje_descuento
        self.lineas = lineas

    def calcular_totales(self) -> dict:
        total_neto = 0.0
        total_iva_21 = 0.0
        total_iva_105 = 0.0
        total_final = 0.0

        for linea in self.lineas:
            neto_linea = linea.calcular_neto_con_descuento(self.porcentaje_descuento)
            iva_linea = linea.calcular_iva(self.porcentaje_descuento)

            total_neto += neto_linea
            total_final += neto_linea + iva_linea

            if linea.producto.porcentaje_iva == 0.21:
                total_iva_21 += iva_linea
            elif linea.producto.porcentaje_iva == 0.105:
                total_iva_105 += iva_linea

        return {
            "tipo_comprobante": self.tipo_comprobante,
            "total_neto": round(total_neto, 2),
            "total_iva_21": round(total_iva_21, 2),
            "total_iva_105": round(total_iva_105, 2),
            "total_iva": round(total_iva_21 + total_iva_105, 2),
            "total_final": round(total_final, 2),
        }
