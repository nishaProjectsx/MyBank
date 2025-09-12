"""
URL configuration for mybank project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path
from bankapp import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index,name="index"),
    path('create', views.createAccount,name='create'),
    path('login', views.login,name='login'),
    path('sevice', views.service,name='service'),
    path('deposit', views.deposit,name='deposit'),
    path('withdraw', views.withdraw,name='withdraw'),
    path('checkBalace', views.checkBalance,name='checkBalance'),
    path('balance_list', views.balance_list, name='balance_list'),
    path('transfer', views.transfer, name='transfer'),
    path('ministatement', views.ministatement, name='ministatement'),
    path('miniList', views.miniList, name='miniList'),
    path('password', views.password, name='password'),





]
if settings.DEBUG:
   urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
   urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)