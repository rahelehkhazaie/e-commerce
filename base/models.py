from django.db import models
#from phonenumber_field.modelfields import PhoneNumberField


class Media(models.Model, ):
    telegram = models.URLField(verbose_name='telegram')
    insta = models.URLField(verbose_name='insta')
    x = models.URLField(verbose_name='x')
    phone = models.CharField(max_length=14)
    email = models.EmailField()
    address = models.CharField(max_length=300)
    

    
    





