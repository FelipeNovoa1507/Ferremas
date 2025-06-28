from transbank.webpay.webpay_plus.transaction import WebpayPlusTransaction as Transaction

# Configuración para el ambiente de pruebas
Transaction.commerce_code = "597055555532"
Transaction.api_key = "597055555532"
Transaction.environment = "TEST"  # Ambiente de pruebas

from django.shortcuts import render, redirect
from .transbank_config import Transaction

def iniciar_pago(request):
    buy_order = "orden12345"  # Identificador único del pedido
    session_id = "sesion12345"  # Identificador único de la sesión
    amount = 10000  # Monto total de la compra
    return_url = request.build_absolute_uri('/pagos/confirmar_pago/')  # URL de retorno

    response = Transaction.create(buy_order, session_id, amount, return_url)
    return redirect(response['url'] + '?token_ws=' + response['token'])