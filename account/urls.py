from django.urls import path

from transactions.views import *
from .views import * 
from django.contrib.auth.decorators import login_required

app_name = 'account'


urlpatterns = [
    path('agents', login_required(AgentProfileListView.as_view()), name='agent-list'),    
    path('fisp/transctions', login_required(TransactionListView.as_view()), name='txn'),
    path('fisp/transctions/<int:pk>/details', login_required(AgentProfileDetailView.as_view()), name='txn_details'),
    path('fisp/transctions/search', login_required(SearchResultsListView.as_view()), name='search'),
    path('fisp/transctions/<int:pk>/detail/search', login_required(detail_search_txn), name='search_txn_details'),
    path('deposit/fisp/transctions/<int:pk>', login_required(make_deposit), name='txn_deposit'),
    path('deposit/fisp/transctions/mark_deposits    ', login_required(make_deposits), name='make_deposits'),
    
    path('loading/', login_required(fetchAPI), name='load'),
]
