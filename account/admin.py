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

 

class CustomUserAdmin(UserAdmin):
    list_display = ('email', 'get_full_name', 'phone', 'dob', 'get_status', 'date_joined', 'is_verified')
    search_fields = ('email', 'first_name', 'last_name', 'phone', 'account_type__role')
    list_filter = ('date_joined', 'is_active', 'is_verified')
    list_per_page = 25
    readonly_fields = ('id_front_image', 'id_back_image', 'dob','date_joined')  # Make 'dob' field read-only

    fieldsets = (
        (_('Personal info'), {'fields': ('email', 'password', 'first_name', 'last_name', 'phone', 'province', 'district', 'country')}),
        (_('Permissions'), {'fields': ('agents_to_manage','is_active', 'is_staff', 'is_verified', 'groups', 'user_permissions')}),
        (_('Important dates'), {'fields': ('last_login', 'date_joined')}),
        (_('ID Images'), {'fields': ('id_front_image', 'id_back_image')}),
    )

    ordering = ('email',)  # Specify default ordering by email

    # add_fieldsets = (
    #     (None, {
    #         'classes': ('wide',),
    #         'fields': ('email', 'password1', 'password2', 'is_active', 'is_staff', 'is_verified', 'groups', 'user_permissions'),
    #     }),
    # )

    def get_full_name(self, obj):
        return obj.get_full_name()
    get_full_name.short_description = _('Full Name')

    def get_status(self, obj):
        return obj.get_status()
    get_status.short_description = _('Status')

    def view_profile(self, obj):
        url = reverse('admin:your_app_name_here_user_change', args=[obj.id])
        return format_html('<a href="{}">View Profile</a>', url)
    view_profile.short_description = ''

    def id_front_image(self, obj):
        if obj.id_front:
            return format_html('<img src="{}" style="max-height: 100px; max-width: 100px;" />', obj.id_front.url)
        return _('No Image')
    id_front_image.short_description = _('ID Front Image')

    def id_back_image(self, obj):
        if obj.id_back:
            return format_html('<img src="{}" style="max-height: 100px; max-width: 100px;" />', obj.id_back.url)
        return _('No Image')
    id_back_image.short_description = _('ID Back Image')

# Register the models with the custom admin classes
admin.site.register(AgentType, AgentTypeAdmin)
admin.site.register(AgentProfile, AgentProfileAdmin)
admin.site.register(User, CustomUserAdmin)
