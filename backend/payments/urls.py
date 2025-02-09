from django.urls import path
from .views import make_payment, view_expenses

urlpatterns = [
    path('make-payment/', make_payment, name='make_payment'),
    path('expenses/', view_expenses, name='expenses'),
]
