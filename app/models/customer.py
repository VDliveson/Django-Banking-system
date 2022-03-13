from django.db import models
from .account import Account

class Customer(models.Model):
    first_name = models.CharField(max_length=200)
    last_name=models.CharField(max_length=200)
    password=models.CharField(max_length=200)
    date_of_birth=models.DateField()
    email=models.EmailField(max_length=50)
    mobile=models.IntegerField()
    address=models.CharField(max_length=200)
    pan_number=models.CharField(max_length=20)
    login_id=models.CharField(max_length=10)
    customer_id=models.CharField(max_length=20,primary_key=True)
    
    def register(self):
        self.save()
        
    @staticmethod
    def get_Customer_by_account_number(login_id):
        return Customer.objects.get(login_id=login_id)
    
    @staticmethod
    def get_Customer_by_email(email):
        return Customer.objects.get(email=email)
    

    
    
        

    
    
