# common.py
from account.models import AgentProfile

def get_total_transaction_amount(agent):
    # Calculate the total transaction amount for this agent
    total_amount = FispTransaction.objects.filter(agent=agent).aggregate(
        total_trans_amount=Sum('transAmount')
    )['total_trans_amount'] or 0

    return total_amount
