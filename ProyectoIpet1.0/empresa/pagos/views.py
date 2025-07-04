from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_exempt
from django.urls import reverse
from transbank.webpay.webpay_plus.transaction import Transaction
from transbank.common.options import WebpayOptions
from transbank.common.integration_type import IntegrationType
from cliente.carrito import Carrito
from django.contrib.auth.decorators import login_required
import uuid

@login_required
def iniciar_pago(request):
    try:
        carrito = Carrito(request)
        monto = 0
        for item in carrito.carrito.values():
            monto += item['precio_unitario'] * item['cantidad']

        buy_order = f'{request.user.id}{request.user.last_login.timestamp()}'
        session_id = str(request.user.id)
        return_url = request.build_absolute_uri('/pagos/confirmar_pago/')

        options = WebpayOptions(
            commerce_code='597055555532',  # código de prueba
            api_key='579B532A7440BB0C9079DED94D31EA1615BACEB56610332264630D42D0A36B1C',  # clave de prueba
            integration_type=IntegrationType.TEST
        )

        response = Transaction(options).create(buy_order, session_id, monto, return_url)
        url = response['url']
        token = response['token']

        return redirect(response['url'] + '?token_ws=' + response['token'])
    
    except Exception as e:
        print("💥 Error al iniciar el pago:", e)
        return render(request, 'pagos/error.html', {'error': str(e)})



@csrf_exempt
def confirmar_pago(request):
    token = request.POST.get('token_ws') or request.GET.get('token_ws')
    if not token:
        return redirect('carrito')  # Usa el nombre de la URL de tu carrito

    try:
        options = WebpayOptions(
            commerce_code='597055555532',
            api_key='579B532A7440BB0C9079DED94D31EA1615BACEB56610332264630D42D0A36B1C',
            integration_type=IntegrationType.TEST
        )
        response = Transaction(options).commit(token)

        if response['status'] == 'AUTHORIZED':
            Carrito(request).limpiar_carrito()
        return render(request, 'pagos/confirmar_pago.html', {
            'response': response,
            'es_confirmacion_pago': True
        })
    except Exception as e:
        return render(request, 'pagos/error.html', {'error': str(e)})