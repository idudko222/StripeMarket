from django.contrib import admin
from django.urls import path
from payment import views
    

urlpatterns = [
    path('admin/', admin.site.urls),
    # Для одиночных товаров
    path('item/<int:id>/', views.item_detail, name='item_detail'),
    path('buy/<int:id>/', views.buy_item, name='buy_item'),
]
