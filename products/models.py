from django.db import models
import os
import random

# Create your models here.

def get_filename_ext(filepath):
    base_name = os.path.basename(filepath)
    name , ext = os.path.splitext(base_name)
    return name,ext

def upload_image_path(instance,filename):
        new_filename = random.randint(1,100000000000000000)
        name , ext = get_filename_ext(filename)
        final_filename = '{new_filename}/{ext}'.format(new_filename=new_filename,ext=ext)
        return "products/{new_filename}/{final_filename}".format(new_filename=new_filename,final_filename=final_filename)

class Product(models.Model):
    title = models.CharField(max_length=20)
    description = models.TextField()
    price = models.DecimalField(max_digits=20,decimal_places=2,default=27.99)
    image = models.ImageField(upload_to=upload_image_path ,null=True,blank=True)
    def __str__(self):
        return self.title