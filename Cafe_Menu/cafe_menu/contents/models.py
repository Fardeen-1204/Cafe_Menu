from django.db import models
from django.core.exceptions import ValidationError

# Create your models here.
class home_text(models.Model):
    description = models.TextField()

    def __str__(self):
        return self.description[:8]
    def save(self, *args, **kwargs):
        if not self.pk and home_text.objects.exists():
            raise ValidationError("Only one description instance is allowed.")
        super().save(*args, **kwargs)


class hot_menu(models.Model):
    name = models.CharField(max_length=100)
    small_price= models.IntegerField()
    large_price= models.IntegerField()
    image = models.ImageField(upload_to='menu_images/')

    def __str__(self):
        return self.name
    
class cold_menu(models.Model):
    name = models.CharField(max_length=100)
    small_price= models.IntegerField()
    large_price= models.IntegerField()
    image = models.ImageField(upload_to='menu_images/')

    def __str__(self):
        return self.name
    
class desert_menu(models.Model):
    name = models.CharField(max_length=100)
    price= models.IntegerField()
    image = models.ImageField(upload_to='menu_images/')

    def __str__(self):
        return self.name
    

class about_us(models.Model):
    description = models.TextField()
    
    def __str__(self):
        return self.description[:8]
    def save(self, *args, **kwargs):
        if not self.pk and about_us.objects.exists():
            raise ValidationError("Only one about instance is allowed.")
        super().save(*args, **kwargs)

class contact_details(models.Model):
    phone_number = models.CharField(max_length=15)
    email = models.EmailField()
    address = models.TextField()
    add_url = models.URLField(null=False,blank=False,default="https://www.google.com/maps")

    def __str__(self):
        return self.email
    def save(self, *args, **kwargs):
        if not self.pk and contact_details.objects.exists():
            raise ValidationError("Only one Contact Details instance is allowed.")
        super().save(*args, **kwargs)

class contact_form(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    message = models.TextField()

    def __str__(self):
        return self.name