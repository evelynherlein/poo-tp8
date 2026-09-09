from factura import Factura


class ImpresorFacturaConsola:
    """
    Pure Fabrication: solo sabe presentar datos, no calcular.
    Recibe una Factura y la muestra formateada por consola.
    """

    def imprimir(self, factura: Factura):
        print("=" * 70)
        print(f" FACTURA N°: {factura.numero} | CLIENTE: {factura.cliente}")
        print("=" * 70)
        print(f"{'Producto':<22} {'Cant':<5} {'P.Unit':<10} {'Subtotal':<10} {'Desc.':<10} {'Total':<10}")
        print("-" * 70)

        for linea in factura.lineas:
            subtotal = linea.calcular_subtotal_bruto()
            desc = linea.calcular_monto_descuento()
            neto = linea.calcular_subtotal_neto()
            print(
                f"{linea.producto.nombre:<22} {linea.cantidad:<5} "
                f"${linea.producto.precio_unitario:<9.2f} "
                f"${subtotal:<9.2f} ${desc:<9.2f} ${neto:<9.2f}"
            )

        print("-" * 70)
        print(f"Subtotal Bruto:     ${factura.calcular_total_bruto():.2f}")
        print(f"Total Descuentos:   ${factura.calcular_total_descuentos():.2f}")
        print(f"TOTAL A PAGAR:      ${factura.calcular_total_neto():.2f}")
        print("=" * 70 + "\n")
