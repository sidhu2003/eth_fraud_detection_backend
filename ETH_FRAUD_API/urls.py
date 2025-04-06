# blockchain_api/urls.py
from django.urls import path, include
from django.contrib import admin
urlpatterns = [
    path('api/accounts/', include('accounts.urls')),
    path('api/tx/', include('transactions.urls')),
    path('admin/', admin.site.urls),
]
