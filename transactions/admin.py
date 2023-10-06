from django.contrib import admin
from .models import FispTransaction
import django_filters


@admin.register(FispTransaction)
class FispTransactionAdmin(admin.ModelAdmin):
    list_display = ('transAdt', 'numberOfFarmers','isDeposited','created_at', 'transAmount', 'agent', 'timestamp')
    list_filter = ('isSuccess','isDeposited', 'agent')
    search_fields = ('transAdt', 'agent__user__first_name' , 'agent__user__last_name')  # Assuming AgentProfile has a user field

    # list_per_page = 25
    list_select_related = ('agent',)

    readonly_fields = ('timestamp', 'updated')

    actions = ['add_deposit','remove_deposit' ]

    def add_deposit(self,request, queryset):
        queryset.update(isDeposited=True)
        
    def remove_deposit(self,request, queryset):
        queryset.update(isDeposited=False)
    
 

    # fieldsets = (
    #     ('Transaction Details', {
    #         'fields': ('transAdt', 'numberOfFarmers', 'isSuccess', 'transAmount', 'totalCommis',
    #                    'transCommisAgent', 'transOldBalance', 'transNewBalance', 'transNewComBalance', 'transOldComBalance')
    #     }),
    #     ('Agent Details', {
    #         'fields': ('agent',)
    #     }),
    #     ('Timestamps', {
    #         'fields': ('timestamp', 'updated'),
    #         'classes': ('collapse',),
    #     }),
    # )

    def get_queryset(self, request):
        # Optimize database queries by selecting related fields
        return super().get_queryset(request).select_related('agent')

    def transAmount_formatted(self, obj):
        # Custom method to format the transaction amount
        return f"${obj.transAmount:.2f}"
    transAmount_formatted.short_description = 'Transaction Amount'

# admin.site.register(FispTransaction, FispTransactionAdmin)
