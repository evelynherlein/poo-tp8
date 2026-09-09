from typing import Dict
from factura import Factura
from producto import Producto
from descuento import Descuento
from impresor_factura_consola import ImpresorFacturaConsola


class GestorDeVentas:
    """
    GRASP Creator:
    - Crea instancias de Factura, ya que coordina el proceso de venta.
    - Administra y conoce el catálogo completo de Productos.

    De esta forma, Factura no necesita conocer el catálogo; solo recibe
    el Producto correspondiente a cada línea que se le pide agregar.
    """

    def __init__(self):
        self._catalogo: Dict[str, Producto] = {}
        self._impresor = ImpresorFacturaConsola()

    # --- Gestión del catálogo de Productos ---

    def agregar_producto_catalogo(self, producto: Producto):
        """Registra un nuevo Producto en el catálogo."""
        self._catalogo[producto.codigo] = producto

    def buscar_producto(self, codigo: str) -> Producto:
        """Busca y retorna un Producto por su código."""
        producto = self._catalogo.get(codigo)
        if producto is None:
            raise ValueError(f"Producto con código '{codigo}' no encontrado en el catálogo.")
        return producto

    # --- Creación y manejo de Facturas ---

    def crear_factura(self, numero: str, cliente: str) -> Factura:
        """Creator: instancia y retorna una nueva Factura."""
        return Factura(numero, cliente)

    def agregar_linea_a_factura(self, factura: Factura, codigo_producto: str,
                                cantidad: int, descuento: Descuento = None):
        """
        Busca el Producto en el catálogo y delega a Factura
        la creación de la LineaFactura correspondiente (GRASP Creator).
        """
        producto = self.buscar_producto(codigo_producto)
        factura.agregar_linea(producto, cantidad, descuento)

    def imprimir_factura(self, factura: Factura):
        """Delega la impresión al ImpresorFacturaConsola (Pure Fabrication)."""
        self._impresor.imprimir(factura)
