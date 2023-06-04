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
from django.urls import path
from django.contrib import admin
from app_menus import views as am
from app_customers import views as acus
from app_accounts import views as aac
urlpatterns = [
    path('admin/', admin.site.urls),
    path('menus/',am.list_menu, name="menu_list"),
    path('menus/add/',am.add_menu, name = 'menu-add'),
    path('menus/edit/',am.edit_menu, name = 'menu-edit'),
    path('menus/show/',am.show_menu, name = 'menu-show'),
    path('cus/create/',acus.c_create, name = 'cus-create'),
    path('cus/edit/',acus.c_edit, name = 'cus-edit'),
    path('cus/index/',acus.c_index, name = 'cus-index'),
    path('cus/show/',acus.c_show, name = 'cus-show'),
    path('acc/login/',aac.ac_login, name = 'ac-login'),
    path('acc/profile/',aac.ac_profile, name = 'ac-profile'),
    path('acc/register/',aac.ac_register, name = 'ac-register'),
]
