from django.shortcuts import render,redirect
from .models import *
from account.models import AgentProfile
from rest_framework import viewsets
from django.views.generic import ListView
from django_filters.views import FilterView
from datetime import datetime, timedelta
from django.shortcuts import get_object_or_404
from django.db.models import Sum
from .forms import *
from django.db.models import Q
from decimal import Decimal
from django.http import HttpResponse

class TransactionListView(ListView):
    model = FispTransaction
    template_name = 'control/transactions_list.html' 
    context_object_name = 'transactions'
    form_class = FilterForm
    paginate_by = 15

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['agents'] = AgentProfile.objects.all()
        return context
 
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        agents_to_manage = AgentProfile.objects.all()
        # Calculate the total transAmount for the filtered queryset
        total_trans_amount = self.get_queryset().aggregate(total_amount=models.Sum('transAmount'))['total_amount']
        deposited_amount =  FispTransaction.objects.filter(isDeposited=True).aggregate(total_amount=Sum('transAmount'))['total_amount']
        try:
            amount = total_trans_amount - deposited_amount
        except:
            amount = 0
        context['form'] = self.form_class(user=self.request.user)  # Add it to the context
        context['total_amount'] = total_trans_amount  # Add it to the context
        context['deposited_amount'] = deposited_amount  # Add it to the context
        context['total_transaction_count'] = self.get_queryset().count()  # Add it to the context
        context['deposited_await'] = amount# Add it to the context
        context['agents'] = AgentProfile.objects.all() #Add it to the context
        return context
 
class SearchResultsListView(ListView):
    model = FispTransaction
    template_name = 'control/transactions_search.html' 
    context_object_name = 'transactions'
    form_class = FilterForm

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['agents'] = AgentProfile.objects.all()
        return context

    def get_queryset(self):
        queryset = super().get_queryset()
        name = self.request.GET.get('q')
        start_date = self.request.GET.get('timestamp')
        end_date = self.request.GET.get('date_to')
        agent_id = self.request.GET.get('agent')

        if name:
            queryset = queryset.filter(
                Q(agent__first_name__icontains=name)|
                Q(agent__last_name__icontains=name)|
                Q(agent__code__icontains=name)|
                Q(agent__phonenumber__icontains=name)
            )
            
        if agent_id == 'all':
            if start_date == end_date:
                queryset = queryset.filter(created_at__date=start_date)
            else:
                if start_date:
                    queryset = queryset.filter(created_at__gte=start_date)    
                if end_date:
                    queryset = queryset.filter(created_at__lte=end_date)
            
        elif agent_id != 'all':
            if start_date is None and end_date is None:
                queryset = queryset.filter(agent_id=agent_id)
            
            if agent_id:
                queryset = queryset.filter(agent_id=agent_id)
            
            if start_date == end_date:
                queryset = queryset.filter(created_at__date=start_date)
            else:
                if start_date:
                    queryset = queryset.filter(created_at__gte=start_date)
                
                if end_date:
                    queryset = queryset.filter(created_at__lte=end_date)
        return queryset
 
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        agents_to_manage = AgentProfile.objects.all()
        # Calculate the total transAmount for the filtered queryset
        # queryset = self.get_queryset()
        total_trans_amount = self.get_queryset().aggregate(total_amount=models.Sum('transAmount'))['total_amount']
        # deposited_amount =  FispTransaction.objects.filter(isDeposited=True, id=self.get_queryset().id) 
        total_deposited_amount_amount = []
        print(self.get_queryset())
        for x in FispTransaction.objects.all():
            if x in  self.get_queryset():
                if x.isDeposited:
                    total_deposited_amount_amount.append(int(x.transAmount))
        try:
            amount = total_trans_amount - sum(total_deposited_amount_amount)
        except:
            amount = 0
 
        context['form'] = self.form_class(user=self.request.user)  # Add it to the context
        context['total_amount'] = total_trans_amount  # Add it to the context
        context['deposited_amount'] = sum(total_deposited_amount_amount)  # Add it to the context
        context['total_transaction_count'] = self.get_queryset().count()  # Add it to the context
        context['deposited_await'] = amount# Add it to the context
        context['agents'] = AgentProfile.objects.all() #Add it to the context
        return context

def make_deposit(request, pk):
    txn = FispTransaction.objects.get(pk=pk)
    txn.isDeposited = True
    txn.save()
    total_amount = txn.aggregate(total_amount=models.Sum('transAmount'))['total_amount']
    context ={
        'transactions':txn,
        'total_amount':total_amount,
        'deposited_amount':total_amount,
        'total_transaction_count':txn.count(),
        'deposited_await':total_amount - total_amount ,
    }
    return render(request, 'control/transactions_search.html', context)

def make_deposits(request):
    if request.method == 'POST':
        # Get a list of selected transaction IDs from the form
        selected_transaction_ids = request.POST.getlist('selected_transactions')

        # Update the isDeposited field for selected transactions
        txn = FispTransaction.objects.filter(pk__in=selected_transaction_ids) 
        txn.update(isDeposited=True)
        total_amount = txn.aggregate(total_amount=models.Sum('transAmount'))['total_amount']
        context ={
                'transactions':txn,
                'total_amount':total_amount,
                'deposited_amount':total_amount,
                'total_transaction_count':txn.count(),
                'deposited_await':total_amount - total_amount ,
            }
        
                # agents_to_manage = AgentProfile.objects.all()
        # Calculate the total transAmount for the filtered queryset
        # total_trans_amount = self.get_queryset().aggregate(total_amount=models.Sum('transAmount'))['total_amount']
        # deposited_amount =  FispTransaction.objects.filter(isDeposited=True).aggregate(total_amount=Sum('transAmount'))['total_amount']
        # try:
        #     amount = total_trans_amount - deposited_amount
        # except:
        #     amount = 0
        # context['form'] = self.form_class(user=self.request.user)  # Add it to the context
        # context['total_amount'] = total_trans_amount  # Add it to the context
        # context['deposited_amount'] = deposited_amount  # Add it to the context
        # context['total_transaction_count'] = self.get_queryset().count()  # Add it to the context
        # context['deposited_await'] = amount# Add it to the context
        # context['agents'] = AgentProfile.objects.all() #Add it to the context
        # Redirect to a confirmation page or the original page
        return render(request, 'control/transactions_search.html', context) # redirect('account:search')  # Change 'confirmation_page' to your actual URL
