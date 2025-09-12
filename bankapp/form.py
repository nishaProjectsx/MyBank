from django import forms
from django.db.models import *
from bankapp.models import *
import random
class MysbForm(forms.ModelForm):
    class Meta:
        model = Mysb
        exclude = ['accno']

    def save(self, commit=True):
        instance = super().save(commit=False)  
        max_accno = Mysb.objects.aggregate(Max('accno'))['accno__max']
        next_accno = 1001 if max_accno is None else max_accno + 1
        instance.accno = next_accno 
        if commit:
            instance.save()                        

        return instance
    
   
class DepositForm(forms.ModelForm):
    class Meta:
        model = Deposit
        fields = '__all__'

class WithdrawForm(forms.ModelForm):
    class Meta:
        model = Withdraw
        fields = '__all__'

class BalanceForm(forms.ModelForm):
    class Meta:
        model = BalancCheck
        fields = '__all__'


class TransferForm(forms.ModelForm):
    class Meta:
        model = Transfer
        fields = '__all__'


class MiniForm(forms.ModelForm):
    class Meta:
        model = MiniStatement
        fields = '__all__'

class PasswordForm(forms.ModelForm):
    class Meta:
        model = ChangePassword
        fields = '__all__'

