"""project_restro_menu URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.urls import path,include
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static

from app_customers import views as acus
from app_accounts import views as aac
urlpatterns = [
    path('admin/', admin.site.urls),
    path('menus/',include('app_menus.urls')),
    path('cus/create/',acus.c_create, name = 'cus-create'),
    path('cus/edit/',acus.c_edit, name = 'cus-edit'),
    path('cus/index/',acus.c_index, name = 'cus-index'),
    path('cus/show/',acus.c_show, name = 'cus-show'),
    path('',include('app_accounts.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)