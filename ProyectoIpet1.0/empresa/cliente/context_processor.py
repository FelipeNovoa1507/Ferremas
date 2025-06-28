def total_carrito(request):
    total = 0
    if request.user.is_authenticated:
        if "carrito" in request.session:
            for key, value in request.session["carrito"].items():
                total += int(value["precio_unitario"])
    return {"total_carrito": total}

def total_listaDeseos(request):
    total = 0
    if request.user.is_authenticated:
        if "listaDeseos" in request.session:
            for key, value in request.session["listaDeseos"].items():
                total += 1
    return {'total_listaDeseos': total}