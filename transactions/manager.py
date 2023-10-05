from django.db import models

class FispTransactionManager(models.Manager):
    def get_total_trans_amount(self):
        return self.aggregate(total_trans_amount=models.Sum('transAmount'))['total_trans_amount'] or 0
    
    def total_deposited_transaction_amount(self):
        return self.filter(isDeposited=True).aggregate(total_amount=models.Sum('transAmount'))['total_amount'] or 0

    def deposited_transaction_count(self):
        return self.filter(isDeposited=True).count()