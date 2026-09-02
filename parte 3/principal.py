from producto import Producto
from detalle_factura import DetalleFactura
from factura import Factura
from descuentos import (
    SinDescuento,
    DescuentoPorVolumen,
    DescuentoPorCategoria,
    DescuentoFijoPorcentaje,
)


def main():
    # 1. Creación de Productos
    prod1 = Producto("P001", "Notebook Gamer", 120000.0, "Electrónica")
    prod2 = Producto("P002", "Mouse Inalámbrico", 5000.0, "Accesorios")
    prod3 = Producto("P003", "Teclado Mecánico", 15000.0, "Electrónica")
    prod4 = Producto("P004", "Cuaderno A4", 1200.0, "Librería")

    # 2. Creación de Estrategias de Descuento (Polimorfismo GRASP)
    desc_volumen = DescuentoPorVolumen(umbral_cantidad=5, porcentaje=15.0)  # 15% desc si >= 5 unidades
    desc_categoria_electro = DescuentoPorCategoria(categoria_promocionada="Electrónica", porcentaje=10.0) # 10% desc en Electrónica
    desc_fijo_oferta = DescuentoFijoPorcentaje(porcentaje=20.0)             # 20% desc directo

    # 3. Creación de Factura y agregado de ítems con Descuentos Dinámicos
    factura1 = Factura("0001-00004589", "Juan Pérez")

    # Item 1: Notebook con Descuento por Categoría (Electrónica)
    factura1.agregar_detalle(DetalleFactura(prod1, cantidad=1, descuento=desc_categoria_electro))

    # Item 2: 6 Mouses (Aplica Descuento por Volumen al ser >= 5)
    factura1.agregar_detalle(DetalleFactura(prod2, cantidad=6, descuento=desc_volumen))

    # Item 3: Teclado con Descuento Fijo de Oferta
    factura1.agregar_detalle(DetalleFactura(prod3, cantidad=1, descuento=desc_fijo_oferta))

    # Item 4: Cuaderno A4 Sin Descuento
    factura1.agregar_detalle(DetalleFactura(prod4, cantidad=3, descuento=SinDescuento()))

    # 4. Impresión y Cálculo Polimórfico de la Factura
    factura1.imprimir_factura()


if __name__ == "__main__":
    main()
