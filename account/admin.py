from django.contrib import admin
from django.utils.html import format_html
from django.urls import reverse
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.admin import UserAdmin
from .models import AgentType, AgentProfile, User

class AgentTypeAdmin(admin.ModelAdmin):
    list_display = ('title', 'commission', 'salary', 'timestamp', 'updated')
    search_fields = ('title',)
    list_filter = ('timestamp', 'updated')
    list_per_page = 25

class AgentProfileAdmin(admin.ModelAdmin):
    list_display = ('phonenumber', 'last_name', 'phonenumber', 'agent_type', 'dob', 'province', 'district', 'timestamp', 'updated')
    search_fields = ('first_name', 'last_name', 'phonenumber', 'agent_type__title')
    list_filter = ('timestamp', 'updated', 'agent_type')
    list_per_page = 25

 

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('email','first_name', 'last_name','country',)
    search_fields = ('first_name','email','last_name') 
 
    actions = ['verify','unverify','activate' ,'deactivate' ]
    
    def verify(self, queryset):
        queryset.update(is_verified=True)
        
    def unverify(self, queryset):
        queryset.update(is_verified=False)
        
    def activate(self, queryset):
        queryset.update(is_active=True)
        
    def deactivate(self, queryset):
        queryset.update(is_active=False)


# Register the models with the custom admin classes
admin.site.register(AgentType, AgentTypeAdmin)
admin.site.register(AgentProfile, AgentProfileAdmin)
