from django.contrib import admin
from django.urls import path
from payment import views
from cart import views as cart_views

urlpatterns = [
    path('admin/', admin.site.urls),
    # Для одиночных товаров
    path('item/<int:id>/', views.item_detail, name='item_detail'),
    path('buy/<int:id>/', views.buy_item, name='buy_item'),
    # list товаров
    path('items', views.item_list, name='item_list'),
    # Управление корзиной
    path(r'^$', cart_views.cart_detail, name='cart_detail'),
    path(r'^add/(?P<product_id>\d+)/$', cart_views.cart_add, name='cart_add'),
    path(r'^remove/(?P<product_id>\d+)/$', cart_views.cart_remove, name='cart_remove'),
    path('cart/checkout/', cart_views.cart_checkout, name='cart_checkout'),
    path('stripe-webhook/', cart_views.stripe_webhook, name='stripe-webhook'),
]
