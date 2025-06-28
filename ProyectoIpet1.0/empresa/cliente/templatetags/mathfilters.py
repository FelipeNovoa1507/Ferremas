from django import template

register = template.Library()

@register.filter
def multiply(value, arg):
    return value * arg


@register.filter
def calcular_descuento(precio, precio_oferta):
    return round((precio - precio_oferta) / precio * 100)