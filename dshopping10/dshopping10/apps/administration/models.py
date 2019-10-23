from django.db import models

# Create your models here.

class Gender (models.Model):
    tittle = models.CharField ('Tittle', max_length=25)
    description = models.TextField ('Description')
    def __str__(self):
        return self.tittle

class Country (models.Model):
    tittle = models.CharField ('Name', max_length=50)
    abbreviation = models.CharField ('Abreviation', max_length=4)
    class Meta:
        verbose_name = 'Country'
        verbose_name_plural = 'Countries'
    def __str__(self):
        return self.tittle

class Categories (models.Model):
    tittle = models.CharField ('Tittle', max_length=100)
    description = models.TextField ('Description')
    def __str__(self):
        return self.tittle

class Products (models.Model):
    tittle = models.CharField ('Tittle', max_length=100)
    description = models.TextField ('Description')
    id_category = models.ForeignKey (Categories, on_delete=models.CASCADE)
    id_country = models.ForeignKey (Country, on_delete=models.CASCADE)
    photo = models.ImageField('Image client', null=True, blank=True, upload_to='Authors/')
    quantity = models.IntegerField ('Quantity', max_length=15)
    def __str__(self):
        return '{0}{1}{2}'.format(self.tittle,', ',self.quantity)

class Clients (models.Model):
    firstname = models.CharField ('First name', max_length=150)
    lastname = models.CharField ('Last name', max_length=150)
    id_gender = models.ForeignKey (Gender, on_delete=models.CASCADE)
    phone = models.IntegerField ('Number', max_length=15) 
    email = models.EmailField ('E-mail', max_length=200)
    password = models.CharField ('Password', max_length=500)
    id_country = models.ForeignKey (Country, on_delete=models.CASCADE)
    photo = models.ImageField('Image client', null=True, blank=True, upload_to='Authors/')
    credit_card_number = models.IntegerField ('Credit card number')
    class Meta:
        verbose_name = 'Client'
        verbose_name_plural = 'Clients'
    def __str__(self):
        return '{0}{1}{2}'.format(self.lastname,', ',self.firstname)


class Shopping (models.Model):
    id_product = models.ForeignKey (Products, on_delete=models.CASCADE)
    id_cliente = models.ForeignKey (Clients, on_delete=models.CASCADE)
    shopping_date = models.DateField (auto_now_add=True)
    
    def __int__(self):
        return '{0}{1}{2}'.format(self.id_cliente,', ',self.id_product)
    
 
  
