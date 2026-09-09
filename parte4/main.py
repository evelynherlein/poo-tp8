from producto import Producto
from gestor_de_ventas import GestorDeVentas
from descuento_por_categorias import DescuentoPorCategorias
from descuento_por_volumen import DescuentoPorVolumen


def main():
    # 1. Crear el GestorDeVentas (coordina todo el proceso de venta)
    gestor = GestorDeVentas()

    # 2. GestorDeVentas administra el catálogo de Productos (GRASP Creator)
    gestor.agregar_producto_catalogo(Producto("P001", "Notebook Gamer",    120000.0, "Electrónica"))
    gestor.agregar_producto_catalogo(Producto("P002", "Mouse Inalámbrico",   5000.0, "Accesorios"))
    gestor.agregar_producto_catalogo(Producto("P003", "Teclado Mecánico",   15000.0, "Electrónica"))
    gestor.agregar_producto_catalogo(Producto("P004", "Cuaderno A4",         1200.0, "Librería"))

    # 3. Crear estrategias de descuento (Polimorfismo GRASP)
    desc_electro  = DescuentoPorCategorias(categoria_promocionada="Electrónica", porcentaje=10.0)
    desc_volumen  = DescuentoPorVolumen(umbral_cantidad=5, porcentaje=15.0)

    # 4. GestorDeVentas crea la Factura (GRASP Creator)
    factura1 = gestor.crear_factura("0001-00004589", "Juan Pérez")

    # 5. GestorDeVentas busca el Producto en el catálogo y Factura crea cada LineaFactura (GRASP Creator)
    gestor.agregar_linea_a_factura(factura1, "P001", cantidad=1, descuento=desc_electro)   # 10% desc Electrónica
    gestor.agregar_linea_a_factura(factura1, "P002", cantidad=6, descuento=desc_volumen)   # 15% desc por volumen
    gestor.agregar_linea_a_factura(factura1, "P003", cantidad=1, descuento=desc_electro)   # 10% desc Electrónica
    gestor.agregar_linea_a_factura(factura1, "P004", cantidad=3)                           # Sin descuento

    # 6. Imprimir la factura (delegado a ImpresorFacturaConsola)
    gestor.imprimir_factura(factura1)


if __name__ == "__main__":
    main()
