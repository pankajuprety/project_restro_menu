from django.urls import path
from app_customers import views
urlpatterns = [
    path('cus/create/',views.c_create, name = 'cus-create'),
    path('cus/edit/',views.c_edit, name = 'cus-edit'),
    path('cus/index/',views.c_index, name = 'cus-index'),
    path('cus/show/',views.c_show, name = 'cus-show'),
]