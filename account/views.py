from django.shortcuts import render,redirect
# Import necessary modules
from django.db.models import Q
from django.views.generic import ListView,DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from transactions.forms import FilterForm
from transactions.models import FispTransaction
from .models import *
from datetime import datetime
# from transactions.models import * 
import requests
from django.db.utils import IntegrityError

# List view for AgentProfile
class AgentProfileListView(ListView):
    model = AgentProfile
    template_name = 'control/agentprofile_list.html'
    context_object_name = 'agentprofiles'


class AgentProfileDetailView(DetailView):
    model = AgentProfile
    template_name = 'control/agentprofile_detail.html'
    context_object_name = 'agentprofiles'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        txn = FispTransaction.objects.filter(agent=self.get_object())
        context["total_amount"] = FispTransaction.objects.filter(agent=self.get_object()).aggregate(total_amount=models.Sum('transAmount'))['total_amount']
        # context["transactions"] = FispTransaction.objects.filter(agent=self.get_object())
        context["total_transaction_count"] = FispTransaction.objects.filter(agent=self.get_object()).count()
        context["transactions"] = FispTransaction.objects.filter(agent=self.get_object())
        return context
    

def detail_search_txn(request, pk):
    transactions = FispTransaction.objects.filter(agent__pk=pk)
    
    # Initialize variables for search and total amount
    search_query = ""
    total_amount = None

    if request.method == "POST":
        # Retrieve the search query from the POST data
        search_query = request.POST.get('q')

        # Filter transactions based on search query
        transactions = transactions.filter(
            Q(transAdt__icontains=search_query) |
            Q(transAmount__icontains=search_query) |
            Q(leadernumber__icontains=search_query) |
            Q(depositer__icontains=search_query) |
            Q(agent__first_name__icontains=search_query) |
            Q(agent__last_name__icontains=search_query)
        )

        # Calculate the total amount for the filtered transactions
        total_amount = transactions.aggregate(total_amount=models.Sum('transAmount'))['total_amount']

        deposited_amount = transactions.aggregate(total_amount=Sum('transAmount'))['total_amount']
        print('total_amount',total_amount)
        print('deposited_amount',deposited_amount)
        # deposited_amount = transactions.aggregate(total_amount=models.Sum('transAmount'))['total_amount']
        # deposited_await = total_amount - deposited_amount 
        context = {
            'form': FilterForm(user=request.user),
            'total_amount': total_amount,
            'transactions':transactions,
            # 'my_agents':agents_to_manage,
            'deposited_amount':deposited_amount ,
            'deposited_await':'deposited_await',
            'total_transaction_count': transactions.count(),
        }

        return render(request, 'control/transactions_search.html', context)
    else:
        form = FispTransaction()

    return render(request, 'control/transactions_search.html', {
        'transactions': transactions,
    })



def fetchAPI(request):
    # API endpoint
    base_url = "https://fisp.ekamo.co.zm/api/fisp/transactions"
    
    # Initialize variables
    page = 1
    all_data_fetched = False
    while not all_data_fetched:
        # Construct the URL for the current page
        url = f"{base_url}?page={page}"

        # Send a GET request to the API
        response = requests.get(url)

        if response.status_code == 200:
            api_data = response.json()
            transactions_data = api_data.get("data", [])

            if not transactions_data:
                # No more data on this page, exit the loop
                all_data_fetched = True
                continue

            for transaction_item in transactions_data:
                datetime_string  =  transaction_item.get("created_at", "")
                # Extract data from the API response
                trans_adt = transaction_item.get("transAdt", "")
                number_of_farmers = transaction_item.get("numberOfFarmers", 0)
                leadernumber = transaction_item.get("leadernumber", 0)  # Correct field name
                depositer = transaction_item.get("depositer", 0)  # Correct field name
                transRef = transaction_item.get("transRef", 0)
                totalCommis = transaction_item.get("totalCommis", 0)
                transCommisAgent = transaction_item.get("transCommisAgent", 0)
                transNewBalance = transaction_item.get("transNewBalance", 0)
                transOldComBalance = transaction_item.get("transOldComBalance", 0)
                transNewComBalance = transaction_item.get("transNewComBalance", 0)
                transStatus = transaction_item.get("transStatus", "")  # Correct field type
                status = transaction_item.get("status", 0)
                transAmount = transaction_item.get("transAmount", 0)
                created_at = datetime.strptime(datetime_string, "%d-%m-%Y %H:%M:%S")

                status_boolean = False
                if status == 1:  # Example: Map 1 to True, everything else to False
                    status_boolean = True
                else:
                    status_boolean = False

                transOldBalance = transaction_item.get("transOldBalance", 0)
                phone_number = transaction_item.get("phoneNumber", "")  # Add phone_number

                # Check if an agent with the given phone number exists, or create a new one
                agent, created = AgentProfile.objects.get_or_create(
                    phonenumber=phone_number,
                    defaults={
                        'floatLimit': 1000.00,  # Default float limit for new agents
                        # You can set other default values here
                    }
                )

                # Check if the transaction has a successful status before saving it
                if transStatus == "success":
                    # Create and save a new FispTransaction instance
                    transaction = FispTransaction(
                        transAdt=trans_adt,
                        numberOfFarmers=number_of_farmers,
                        transAmount=transAmount,
                        transOldBalance=transOldBalance,
                        leadernumber=leadernumber,
                        depositer=depositer,
                        transRef=transRef,
                        totalCommis=totalCommis,
                        transCommisAgent=transCommisAgent,
                        transNewBalance=transNewBalance,
                        transOldComBalance=transOldComBalance,
                        transNewComBalance=transNewComBalance,
                        created_at=created_at,
                        isSuccess=status_boolean,       
                        agent=agent  # Use the agent as the primary key for the transaction
                        # Set other fields accordingly
                    )
                    try:
                        transaction.save()
                    except IntegrityError:
                        # Duplicate transRef, skip this entry and continue with the next one
                        pass
            # Move to the next page
            page += 1
    return redirect('account:txn')
