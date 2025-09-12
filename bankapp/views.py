from django.shortcuts import render,redirect
from bankapp.form import *
from bankapp.models import *
from decimal import Decimal, InvalidOperation

def index(request):
    return render(request,"index.html")
def service(request):
    return render(request,"service.html")

def miniStatement(request, accno, credit, debit, total_amount):
    print(accno,credit,debit ,total_amount)
    MiniStatement.objects.create(
    accno=accno,
    credit=credit,
    debit=debit,
    total_amount=total_amount 
)

    return render(request, "service.html")



def createAccount(request):
    data = request.POST
    print("data-------",data)
    if request.method == 'POST':
        sform = MysbForm(request.POST, request.FILES)
        if sform.is_valid():
            sform.save()
            return redirect('index')
        else:
            return render(request, "create.html", {'form': sform, 'errors': sform.errors})

    return render(request, "create.html", {'form': MysbForm()})


def login(request):
    if request.method == 'POST':
        pin = request.POST.get('pin')
        accno = request.POST.get('accno')       
        account = Mysb.objects.filter(accno = accno,pin=pin).first()
        if account:
            return redirect('service')  
        else:
            return render(request, "login.html", {'error': 'Invalid Account Number or PIN'}) 

    return render(request, "login.html")

def deposit(request):
    if request.method == 'POST':
        # print('data----',request.POST)
        dform = DepositForm(request.POST)
        if dform.is_valid():
            accno = dform.cleaned_data['accno']
            ammount = dform.cleaned_data['ammount']
            update = Mysb.objects.select_for_update().filter(accno=accno).first()

            if update:
                update.balance += ammount
                print('balance: ',update.balance)
                update.save()
                miniStatement(request, accno, ammount, 0.0, update.balance) 
                return redirect('service')
                
    return render(request,"deposit.html")


def withdraw(request):
    if request.method == 'POST':
        wform = WithdrawForm(request.POST)
        if wform.is_valid():
            accno = wform.cleaned_data['accno']
            ammount = wform.cleaned_data['ammount']
            update = Mysb.objects.select_for_update().filter(accno=accno).first()

            if update:
                if update.balance >= ammount:
                    update.balance -= ammount
                    print('balance: ',update.balance)
                    update.save()
                    miniStatement(request, accno, 0.0, ammount, update.balance) 
                    return redirect('service')
            
    return render(request,"withdraw.html")

def checkBalance(request):
    if request.method =='POST':
        bform = BalanceForm(request.POST)
        pin = request.POST.get('pin')
        accno = request.POST.get('accno')  
        if bform.is_valid():
            balance = Mysb.objects.filter(accno = accno,pin = pin).values_list('balance')
            print(pin)
            print(accno)
            print('balance ---',balance)
            return redirect(f'/balance_list?accno={accno}&pin={pin}')
    return render (request, "checkBalance.html")    

    
def balance_list(request):
    pin = request.GET.get('pin')  
    accno = request.GET.get('accno')
    balance = Mysb.objects.filter(accno=accno, pin=pin).values_list('balance', flat=True).first()
    context = {
        'balance' : balance,
        'accno' : accno
    }

    return render(request,'balance_list.html',context)




def transfer(request):
    if request.method == 'POST':
        accno = request.POST.get('accno')
        pin = request.POST.get('pin')
        haccno = request.POST.get('haccno')
        am = request.POST.get('ammount')
        cam = request.POST.get('cammount')
        ammount = Decimal(am)
        cammount = Decimal(cam)
        context = {}
        if ammount != cammount:
            context['error'] = "Entered amounts do not match."
            return render(request, "transfer.html", context)

        print('all-----',accno,pin,haccno,ammount,cammount)
        tform = TransferForm(request.POST)
        if tform.is_valid():
            sender = Mysb.objects.select_for_update().get(accno=accno, pin=pin)
            receiver = Mysb.objects.select_for_update().get(accno=haccno)
            if sender and receiver:
                if ammount< sender.balance:
                    sender.balance -= ammount
                    receiver.balance += ammount
                    sender.save()
                    receiver.save()
                    miniStatement(request, accno, 0.0, ammount, sender.balance)
                    miniStatement(request, haccno, ammount, 0.0, receiver.balance) 

                    return render( request, 'service.html',{'msg': 'Transection Was Successfully !!!! '})
                else :
                    return render(request,"transfer.html",{'msg1': 'insuffient balance available !!!!'})
                    

    return render(request,"transfer.html")


def ministatement(request):
    if request.method == 'POST':
        accno = request.POST.get('accno')
        return redirect(f'/miniList?accno={accno}')
    return render(request, "mini.html")

    

def miniList(request):
    accno = request.GET.get('accno')
    if accno:
        transactions = MiniStatement.objects.filter(accno=accno).order_by('-id')  
        context = {
            'mform': transactions,
            'accno': accno
        }
        return render(request, "ministatement.html", context)
    return render(request, "ministatement.html")
  




def password(request):
                    

    return render(request,"password.html")





# Create your views here.
