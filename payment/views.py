from django.shortcuts import render, get_object_or_404
from .models import Item
import stripe
from django.conf import settings
from django.http import JsonResponse

stripe.api_key = settings.STRIPE_SECRET_KEY


def item_detail(request, id):
    item = get_object_or_404(Item, id=id)
    return render(
        request, 'item_detail.html', {
            'item': item,
            'stripe_publishable_key': settings.STRIPE_PUBLISHABLE_KEY
        }
    )


def buy_item(request, id):
    item = get_object_or_404(Item, id=id)

    try:
        checkout_session = stripe.checkout.Session.create(
            payment_method_types=['card'],
            line_items=[
                {
                    'price_data': {
                        'currency': 'rub',
                        'product_data': {
                            'name': item.name,
                        },
                        'unit_amount': int(item.price * 100),
                    },
                    'quantity': 1,
                }
            ],
            mode='payment',
            success_url=request.build_absolute_uri('/') + '?success=true',
            cancel_url=request.build_absolute_uri('/') + '?canceled=true',
        )
        return JsonResponse({'sessionId': checkout_session.id})
    except Exception as e:
        return JsonResponse({'error': str(e)}, status=400)


def item_list(request):
    items = Item.objects.all()
    return render(
        request, 'item_list.html', {
            'items': items,
            'stripe_publishable_key': settings.STRIPE_PUBLISHABLE_KEY,
        }
        )
