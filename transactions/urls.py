# urls.py

from django.urls import path
from .views import TransactionListView


app_name = "transactions"

urlpatterns = [
    # Your other URL patterns go here
    path('transactions/', login_required(TransactionListView.as_view()), name='transaction_list'),
]
