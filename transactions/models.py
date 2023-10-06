from django.db import models
from django.urls import reverse
from account.models import AgentProfile
from .manager import FispTransactionManager

# Create your models here.
class FispTransaction(models.Model):
    transRef            = models.CharField(max_length=100, default=None, unique=True)
    transAdt            = models.CharField(max_length = 150)
    numberOfFarmers     = models.IntegerField()
    leadernumber        = models.CharField(max_length=50, null=True,blank=True)
    depositer           = models.CharField(max_length=50, null=True,blank=True)
    isSuccess           = models.BooleanField(default=False)
    isDeposited         = models.BooleanField(default=False)
    transAmount         = models.DecimalField(max_digits=100, decimal_places=2)
    totalCommis         = models.DecimalField(max_digits=100, decimal_places=2, null=True,blank=True)
    transCommisAgent    = models.DecimalField(max_digits=100, decimal_places=2, null=True,blank=True)
    transOldBalance     = models.DecimalField(max_digits=100, decimal_places=2, null=True,blank=True)
    transNewBalance     = models.DecimalField(max_digits=100, decimal_places=2, null=True,blank=True)
    transNewComBalance  = models.DecimalField(max_digits=100, decimal_places=2, null=True,blank=True)
    transOldComBalance  = models.DecimalField(max_digits=100, decimal_places=2, null=True,blank=True)
    created_at          = models.DateTimeField(editable=True, default=None)
    timestamp 	        = models.DateTimeField(auto_now_add=True)
    updated 	        = models.DateTimeField(auto_now=True)
    agent               = models.ForeignKey(AgentProfile, on_delete=models.CASCADE)
  

    objects = FispTransactionManager()  # Attach the custom manager

    class Meta:
        indexes = [
            models.Index(fields=['agent_id']),  # Index for agent_id
            models.Index(fields=['created_at']),  # Index for created_at
        ]
        ordering = ['-created_at']  

    def get_total_txn_amount(self):
        # Calculate the total transaction amount for this instance
        return self.transAmount

    def get_total_amount_deposited(self):
        # Calculate the total amount deposited for this instance
        if self.isDeposited:
            return self.transAmount
        return 0  # If not deposited, return 0

    def get_total_amount_deposited_count(self):
        # Calculate the count of deposits for this instance
        return 1 if self.isDeposited else 0

    def set_is_deposit(self):
        return reverse('account:txn_deposit',  args=[str(self.pk),])




    def get_status(self):
        if self.isSuccess:
            return "Success"
        return  "Failed"

    def get_deposit_status(self):
        if self.isDeposited:
            return "Yes"
        return  "No"
    
    def get_deposit(self):
        if self.isDeposited:
            return True
        return  False


    def __str__(self):
        return f'{self.transAdt} - {self.transAmount}'
    
class AgentExpenses(models.Model): 
    amount              = models.DecimalField(max_digits=100, decimal_places=2)
    agent_given         = models.ForeignKey(AgentProfile, on_delete=models.CASCADE)
    reason              = models.TextField()
    timestamp 	        = models.DateTimeField(auto_now_add=True)
    updated 	        = models.DateTimeField(auto_now=True)


    def __str__(self):
        return f'{self.amount} - {self.agent_given}'
 
   