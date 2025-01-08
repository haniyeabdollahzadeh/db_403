from django.shortcuts import render, get_object_or_404, redirect
from .models import Transaction
from .forms import TransactionForm  
from django.contrib.auth.decorators import login_required


@login_required
def transaction_list(request):
    if request.user.is_superuser:  # اگر کاربر ادمین باشد
        transactions = Transaction.objects.all()
    else:  # اگر دانشجو باشد
        transactions = Transaction.objects.filter(username=request.user)
    return render(request, 'transaction_list.html', {'transactions': transactions})



@login_required
def transaction_detail(request, transaction_id):
    transaction = get_object_or_404(Transaction, id=transaction_id)
    if not request.user.is_superuser and transaction.username != request.user:
        return redirect('transaction-list')  # جلوگیری از دسترسی غیرمجاز
    return render(request, 'transaction_detail.html', {'transaction': transaction})



@login_required
def transaction_create(request):
    if request.method == 'POST':
        form = TransactionForm(request.POST)
        if form.is_valid():
            transaction = form.save(commit=False)
            transaction.username = request.user  # کاربر جاری را به تراکنش نسبت می‌دهیم
            transaction.save()
            return redirect('transaction-list')
    else:
        form = TransactionForm()
    return render(request, 'transaction_form.html', {'form': form})

