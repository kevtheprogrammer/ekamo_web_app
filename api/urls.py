# urls.py
from django.urls import path
from  .ekamo_views import *
from .views import AgentPhoneNumberViewSet,AgentFloatLimitViewSet
app_name = 'account'


urlpatterns = [


    path('agent/<str:phonenumber>/', AgentPhoneNumberViewSet.as_view({'get': 'list'}), name='agent-phone'),
    path('agent/<str:phonenumber>/floatlimit/', AgentFloatLimitViewSet.as_view({'get': 'list'}), name='agent-floatlimit'),
]


