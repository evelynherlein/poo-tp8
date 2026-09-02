class Producto:
    """Representa un producto dentro del sistema comercial."""
    
    def __init__(self, codigo: str, nombre: str, precio_unitario: float, categoria: str):
        self.codigo = codigo
        self.nombre = nombre
        self.precio_unitario = precio_unitario
        self.categoria = categoria

    def __repr__(self):
        return f"Producto({self.codigo}, '{self.nombre}', ${self.precio_unitario:.2f}, Cat: '{self.categoria}')"
