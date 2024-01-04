from django.db import models
from account.models import User


"""COLOR_CHOICES = (
    ('Y', 'yellow'),
    ('R', 'red'),
    ('B', 'blue'),
    ('G', 'green'),
    ('BL', 'black'),
    ('W', 'white'),
    ('P', 'pink'),
    ('PP', 'purple')
)

SIZE_CHIOCES = (
    ('S', 'small'),
    ('L', 'large'),
    ('M', 'medium'),
    ('xl', 'XL'),
    ('2xl', '2XL'),
)"""


class Color(models.Model):
    title = models.CharField(max_length=50)
    
    def __str__(self):
       return self.title

    
class Size(models.Model):
    title = models.CharField(max_length=50)
    
    def __str__(self):
       return self.title
   
   
"""class Image(models.Model):
    title = models.CharField(max_length=50)
    image = models.ImageField(upload_to='images/product')
    
    def __str__(self):
       return self.title"""
    
    
class Category(models.Model):
    parent = models.ForeignKey('self', blank=True, null=True, on_delete=models.CASCADE, related_name='subs')
    title = models.CharField(max_length=50)
    slug = models.SlugField()
    image = models.ImageField(upload_to='images/category')

    def __str__(self):
        return self.title
    
    
class Product(models.Model):
    name = models.CharField(max_length=50)
    category = models.ManyToManyField(Category, blank=True, related_name='products')
    price = models.DecimalField(max_digits=20, decimal_places=2)
    discount = models.IntegerField(default=0)
    og_price = models.DecimalField(max_digits=20, decimal_places=2, default=10)

    color = models.ManyToManyField(Color, related_name='colors')
    size = models.ManyToManyField(Size, related_name='sizes', blank=True)
    image = models.ImageField(upload_to='images/product')
    #color = models.CharField(max_length=50, choices=COLOR_CHOICES,)
    #size = models.CharField(max_length=50, choices=SIZE_CHIOCES, blank=True)
    
    intro = models.CharField(max_length=200)
    description = models.TextField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)
    
    is_special = models.BooleanField(default=False)

    @property 
    def price(self):
        return (self.og_price) - (self.og_price) * (self.discount)/100
    
    def cover(self):
        if self.is_special == True:
            return True

    def __str__(self):
        return self.name
    
   
class Review(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='reviews')
    body = models.CharField(max_length=200)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    
    def __str__(self):
       return self.body[0:100]
   
   
   


    