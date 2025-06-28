import uuid
from django.shortcuts import render, redirect
from transbank.webpay.webpay_plus.transaction import Transaction
from transbank.common.options import WebpayOptions
from transbank.common.integration_type import IntegrationType

# ✅ Configuración global del ambiente de pruebas
options = WebpayOptions(
    commerce_code='597055555536',
    api_key='597055555536',
    integration_type=IntegrationType.TEST
)

def obtener_total_carrito(request):
    return 19990  # Reemplaza con tu lógica real

def iniciar_pago(request):
    buy_order = str(uuid.uuid4())[:26]  # Máximo 26 caracteres
    session_id = str(uuid.uuid4())[:26]
    amount = obtener_total_carrito(request)
    return_url = request.build_absolute_uri('/pagos/respuesta/')

    # ✅ Crear transacción
    response = Transaction(options).create(buy_order, session_id, amount, return_url)

    return redirect(response['url'] + '?token_ws=' + response['token'])

def respuesta_pago(request):
    token = request.GET.get('token_ws')

    response = Transaction(options).commit(token)

    if response['status'] == 'AUTHORIZED':
        return render(request, 'pagos/pago_exitoso.html', {'response': response})
    else:
        return render(request, 'pagos/pago_fallido.html', {'response': response})