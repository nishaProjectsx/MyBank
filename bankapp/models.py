from django.db import models
import random

class Mysb(models.Model):
    accno = models.IntegerField(primary_key=True,unique=True)
    fname = models.CharField(max_length=50)
    laname = models.CharField(max_length=50)
    age = models.IntegerField()
    contact = models.IntegerField()
    adhar = models.IntegerField()
    dob = models.DateField()
    pin = models.IntegerField(blank=True, null=True)
    password = models.CharField(max_length=10)
    balance = models.DecimalField(max_digits=10, decimal_places=2)
    created_date = models.DateTimeField(auto_now_add=True,null=True)


    def __str__(self):
        return self.fname
    
    def save(self, *a, **b):
        if not self.pin:
            self.pin = random.randint(1111, 9999)
        super().save(*a, **b)

# class Statement(models.Model):
#     account_no =models.IntegerChoices()
#     credit = models.IntegerField()
#     debit = models.IntegerField()
#     ref_no = models.IntegerField()
#     cdate = models.DateTimeField(auto_now_add=True,null=True)

#     def __str__(self):
#         return self.fname


# Create your models h
class Deposit(models.Model):
    accno = models.IntegerField(primary_key=True,unique=True)
    ammount = models.IntegerField()


class Withdraw(models.Model):
        accno = models.IntegerField(primary_key=True,unique=True)
        ammount = models.IntegerField()

class BalancCheck(models.Model):
        accno = models.IntegerField(primary_key=True,unique=True)
        pin = models.IntegerField()


class Transfer(models.Model):
    accno = models.IntegerField(primary_key=True,unique=True)
    pin = models.IntegerField()
    haccno = models.IntegerField()
    ammount = models.DecimalField(max_digits=10, decimal_places=2)
    cammount =models.DecimalField(max_digits=10, decimal_places=2)




def generate_ref_no():
    return random.randint(1111, 9999)

class MiniStatement(models.Model):
    accno = models.IntegerField()
    credit = models.DecimalField(max_digits=10, decimal_places=2)
    debit = models.DecimalField(max_digits=10, decimal_places=2)
    total_amount = models.DecimalField(max_digits=10, decimal_places=2)
    ref_no = models.IntegerField(default=generate_ref_no)
    date = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return f"MiniStatement({self.accno}, Ref: {self.ref_no})"


class ChangePassword(models.Model):
     accno = models.IntegerField()
     npassword = models.CharField(max_length=10)
     rpassword = models.CharField(max_length=10)