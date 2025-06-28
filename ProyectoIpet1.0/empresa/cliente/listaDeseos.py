class listaDeseos:
    def __init__(self, request):
        self.request = request
        self.session = request.session
        listaDeseos = self.session.get('listaDeseos')
        if not listaDeseos:
            self.listaDeseos = self.session['listaDeseos'] = {}
        else:
            self.listaDeseos = listaDeseos

    def agregar(self, producto, imagen_url=None):
        id = str(producto.id)
        if imagen_url is None:
            imagen_url = producto.imagen.url
        if id not in self.listaDeseos.keys():
            self.listaDeseos[id] = {
                'imagen': imagen_url,
                'producto_id': producto.id,
                'nombre': producto.nombre,
                'precio': producto.precio,
                'precio_Oferta': producto.precio_Oferta,


            }
        else:
            self.listaDeseos[id]['cantidad'] += 1
        self.guardar_listaDeseos()

    def guardar_listaDeseos(self):
        self.session['listaDeseos'] = self.listaDeseos
        self.session.modified = True

    def eliminar(self, producto):
        id = str(producto.id)
        if id in self.listaDeseos:
            del self.listaDeseos[id]
            self.guardar_listaDeseos()

    def limpiar_listaDeseos(self):
        self.session['listaDeseos'] = {}
        self.session.modified = True