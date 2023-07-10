from django.db import models
from django.utils import timezone
from datetime import datetime

creationDate = datetime.now()
creationDate = timezone.now

# Create your models here.
class Category(models.Model):
    category_title = models.CharField(max_length=100)
    category_code = models.CharField(max_length=20, null= True, blank=False)

    def __str__(self):
        return self.category_title

    class Meta:
        db_table = 'restro_categories'
        ordering = ["-category_title"]

class Menu(models.Model):
    menu_title = models.CharField(max_length=100)
    menu_price = models.FloatField(default=0.00)
    menu_ingredient = models.CharField(max_length=100)
    menu_category =models.ForeignKey(Category, on_delete = models.CASCADE)
    menu_image = models.FileField(upload_to="images/menus/", blank=True, null=True)
    menu_created_at = models.DateTimeField(default = creationDate)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.menu_title + "-" + self.menu_category.category_title

    class Meta:
        db_table = "restro_menus"
        ordering = ["-menu_title"]



class Order(models.Model):
    menu = models.ForeignKey(Menu, on_delete= models.CASCADE)
    quantity = models.IntegerField()
    date = models.DateTimeField(default=creationDate)

    class Meta:
        db_table = "restro_Order"
        ordering = ["-date"]
