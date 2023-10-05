from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf.urls.static import static
from django.conf import settings
from rest_framework.routers import DefaultRouter

from django.contrib import admin
from django.urls import path, include
from api.views import *

router = DefaultRouter()
router.register(r'users', CustomUserViewSet, basename='user')
router.register(r'agent-type', AgentTypeViewSet, basename='agent_type')
router.register(r'agent', AgentPhoneNumberViewSet, basename='agent-phone')
router.register(r'agent', AgentFloatLimitViewSet, basename='agent-floatlimit')
router.register(r'transactions',FispTransactionViewSet, basename='transaction')

urlpatterns = [
    path('admin/fisp/', admin.site.urls),
    path('account/', include('account.urls')),
    path('api/', include(router.urls)),
    path("auth/", include('django.contrib.auth.urls')),
]

urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.MEDIA_URL , document_root = settings.MEDIA_ROOT)
