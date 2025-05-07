# donation_tracker/donations/urls.py

from django.urls import path
from . import views # views.py dosyasındaki view'ları import ediyoruz

app_name = 'donations'  # Bu, URL'leri isimlendirmek ve şablonlarda kolayca referans vermek için kullanılır.

urlpatterns = [
    path('', views.donation_list, name='donation_list'),
    # İleride buraya bağış ekleme, detay gösterme gibi başka URL'ler de ekleyeceğiz.
    # Örneğin: path('ekle/', views.add_donation, name='add_donation'),
]