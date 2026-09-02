class ImpresorFacturaConsola:
    """Pure Fabrication: solo sabe presentar, no calcular."""

    def imprimir(self, datos: dict):
        print(f"Total a Pagar: ${datos['total_final']}")
        print(f"  IVA 21%:   ${datos['total_iva_21']}")
        print(f"  IVA 10.5%: ${datos['total_iva_105']}")
        if datos["tipo_comprobante"] == "A":
            print(f"Detalle IVA total: ${datos['total_iva']}")
