from django.contrib import admin
from django.urls import path, include
import urls
from backend.users import views as user_views
from django.shortcuts import render


urlpatterns = [
    path('admin/', admin.site.urls),
    path('users/', include('backend.users.urls')),
    path('payments/', include('backend.payments.urls')),
    path('expenses/', include('backend.expenses.urls')),
    path('coupons/', include('backend.coupons.urls')),
    path('', user_views.home, name='home'),
]
