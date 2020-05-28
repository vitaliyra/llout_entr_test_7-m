from django.contrib import admin
from django.urls import path, include
from django.views.generic.base import TemplateView # new

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('accounts.urls')), # new
    path('accounts/', include('django.contrib.auth.urls')),
    path('ll', TemplateView.as_view(template_name='home.html'), name='home'),
    path('', include('firstapp.urls')), # new
    
    path('ent_test', include('entry_test.urls')),
]
