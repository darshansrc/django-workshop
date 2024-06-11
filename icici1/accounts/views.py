from django.shortcuts import render, redirect
from .forms import CustomerForm
from .models import Customer

def create_account(request):
    if request.method == 'POST':
        form = CustomerForm(request.POST)
        if form.is_valid():
            customer = form.save()
            return redirect('account_success', account_number=customer.account_number)
    else:
        form = CustomerForm()
    return render(request, 'accounts/create_account.html', {'form': form})

def account_success(request, account_number):
    return render(request, 'accounts/account_success.html', {'account_number': account_number})
