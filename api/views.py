from account.models import User, AgentProfile, AgentType
from .serializers import *
# from rest_framework.decorators import action
from rest_framework import viewsets
# from rest_framework import generics
from transactions.models import FispTransaction
from .serializers import FispTransactionSerializer


 # Create your views here.
class FispTransactionViewSet(viewsets.ModelViewSet):
    queryset = FispTransaction.objects.all()
    serializer_class = FispTransactionSerializer

class CustomUserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = CustomUserSerializer

class AgentTypeViewSet(viewsets.ModelViewSet):
    queryset = AgentType.objects.all()
    serializer_class = AgentTypeSerializer

class AgentFloatLimitViewSet(viewsets.ModelViewSet):
    queryset = AgentProfile.objects.all()
    serializer_class = AgentSerializer

    # ... (other methods
class AgentPhoneNumberViewSet(viewsets.ModelViewSet):
    queryset = AgentProfile.objects.all()
    serializer_class = AgentSerializer
    lookup_field = 'phonenumber'

class AgentFloatLimitViewSet(viewsets.ModelViewSet):
    queryset = AgentProfile.objects.all()
    serializer_class = AgentSerializer
    lookup_field = 'phonenumber'  # Use 'phonenumber' as the lookup field for updating

    def perform_update(self, serializer):
        # You can add custom logic here if needed before updating
        serializer.save()