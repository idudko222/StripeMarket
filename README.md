# Django Stripe E-Commerce

## Описание
Интернет-магазин с интеграцией Stripe для обработки платежей. Поддерживает покупку отдельных товаров, корзину с групповой оплатой и админ-панель для управления товарами.

## Технологии
- Python 3.11+
- Django 5.0+
- Stripe API
- SQLite (для разработки)

## Установка
1. Клонируйте репозиторий:
```bash
git clone https://github.com/idudko222/StripeMarket
cd Stripe
```

2. Создайте и активируйте виртуальное окружение:

```bash
python -m venv venv
source venv/bin/activate  # Для Windows: venv\Scripts\activate
```

3. Установите зависимости:

```bash
pip install -r requirements.txt
```

4. Настройка

```bash
SECRET_KEY=ваш_django_секретный_ключ
STRIPE_PUBLIC_KEY=pk_test_ваш_ключ
STRIPE_SECRET_KEY=sk_test_ваш_ключ
```

4. Примените миграции:

```bash
python manage.py migrate
python manage.py makemigrations
```
### Запуск

``python manage.py runserver``

## Функционал

- Главная страница (/) - редирект на каталог товаров

- Каталог товаров (/items/) - список всех доступных товаров

- Страница товара (/item/<id>/) - детальная информация о товаре

- Корзина (/cart/) - просмотр и управление корзиной

- Оплата (/buy/<id>/ и /cart/checkout/) - обработка платежей через Stripe

## Демо
Живая демонстрация доступна тут:
https://idudko222.pythonanywhere.com/items/