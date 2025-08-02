from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_POST
from payment.models import Item
from .cart import Cart
from .forms import CartAddProductForm
import stripe
from django.conf import settings
from django.http import JsonResponse


@require_POST
def cart_add(request, product_id):
    cart = Cart(request)
    item = get_object_or_404(Item, id=product_id)
    form = CartAddProductForm(request.POST)
    if form.is_valid():
        cd = form.cleaned_data
        cart.add(
            item=item,
            quantity=cd['quantity'],
            update_quantity=cd['update']
            )
    return redirect('cart_detail')


def cart_remove(request, product_id):
    cart = Cart(request)
    item = get_object_or_404(Item, id=product_id)
    cart.remove(item)
    return redirect('cart_detail')


def cart_detail(request):
    cart = Cart(request)
    return render(
        request, 'cart/detail.html', {'cart': cart, 'stripe_publishable_key': settings.STRIPE_PUBLISHABLE_KEY}
        )


def cart_checkout(request):
    cart = Cart(request)

    if not cart:
        return JsonResponse({'error': 'Корзина пуста'}, status=400)

    stripe.api_key = settings.STRIPE_SECRET_KEY

    try:
        line_items = []
        for item in cart:
            line_items.append(
                {
                    'price_data': {
                        'currency': 'rub',
                        'product_data': {
                            'name': item['product'].name,
                        },
                        'unit_amount': int(item['price'] * 100),  # Stripe требует сумму в копейках
                    },
                    'quantity': item['quantity'],
                }
            )

        checkout_session = stripe.checkout.Session.create(
            payment_method_types=['card'],
            line_items=line_items,
            mode='payment',
            success_url=request.build_absolute_uri('/success/'),
            cancel_url=request.build_absolute_uri('/cart/'),
        )

        return JsonResponse({'sessionId': checkout_session.id})

    except Exception as e:
        return JsonResponse({'error': str(e)}, status=400)
