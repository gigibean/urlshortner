from django.db import models


# Create your models here.
class Url(models.Model):
    shorten_id= models.SlugField(max_length= 8, primary_key= True, unique= True)
    original_url= models.URLField(unique= True)
    objects= models.Manager()
    
def __str__(self):
    return self.original_url
