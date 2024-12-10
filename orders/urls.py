from django.urls import path
from . import views

urlpatterns = [
    path('', views.order_pizza, name='order_pizza'),
    path('order/confirmation/<int:order_id>/', views.confirmation_page, name='confirmation_page'),

    path('get-pizza-price/', views.get_pizza_price, name='get_pizza_price'),
    path('order/invoice/<int:order_id>/', views.download_invoice, name='download_invoice'),
    path('download_invoice_excel/<int:order_id>/', views.download_invoice_excel, name='download_invoice_excel'),
]

