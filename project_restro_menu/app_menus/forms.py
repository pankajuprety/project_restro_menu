from django import forms
from app_menus.models import Category,Menu

class CategoryCreateform(forms.ModelForm):
    class Meta:
        fields = ("category_title","category_code")
        model = Category

class MenuCreateForm(forms.ModelForm):
    class Meta:
        fields = ("menu_title","menu_price","menu_ingredient","menu_category","menu_image")
        model = Menu