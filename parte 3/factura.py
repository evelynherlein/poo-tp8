from typing import List
from detalle_factura import DetalleFactura


class Factura:
    """
    Clase principal de facturación.
    Agrupa los detalles y calcula totales consumiendo el polimorfismo de los ítems.
    """
    
    def __init__(self, numero: str, cliente: str):
        self.numero = numero
        self.cliente = cliente
        self.detalles: List[DetalleFactura] = []

    def agregar_detalle(self, detalle: DetalleFactura):
        self.detalles.append(detalle)

    def calcular_total_bruto(self) -> float:
        return sum(item.calcular_subtotal_bruto() for item in self.detalles)

    def calcular_total_descuentos(self) -> float:
        return sum(item.calcular_monto_descuento() for item in self.detalles)

    def calcular_total_neto(self) -> float:
        return sum(item.calcular_subtotal_neto() for item in self.detalles)

    def imprimir_factura(self):
        print("=" * 70)
        print(f" FACTURA N°: {self.numero} | CLIENTE: {self.cliente}")
        print("=" * 70)
        print(f"{'Producto':<22} {'Cant':<5} {'P.Unit':<10} {'Subtotal':<10} {'Desc.':<10} {'Total Item':<10}")
        print("-" * 70)
        
        for item in self.detalles:
            subtotal = item.calcular_subtotal_bruto()
            desc = item.calcular_monto_descuento()
            neto = item.calcular_subtotal_neto()
            print(f"{item.producto.nombre:<22} {item.cantidad:<5} ${item.producto.precio_unitario:<9.2f} ${subtotal:<9.2f} ${desc:<9.2f} ${neto:<9.2f}")
            
        print("-" * 70)
        print(f"Subtotal Bruto:     ${self.calcular_total_bruto():.2f}")
        print(f"Total Descuentos:   ${self.calcular_total_descuentos():.2f}")
        print(f"TOTAL A PAGAR:      ${self.calcular_total_neto():.2f}")
        print("=" * 70 + "\n")
