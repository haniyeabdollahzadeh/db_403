from django.shortcuts import render, get_object_or_404, redirect
from .models import Transaction
from .forms import TransactionForm  
from django.contrib.auth.decorators import login_required


from django.db import connection


from django.db import connection
from django.shortcuts import render
from django.contrib.auth.decorators import login_required


@login_required
def transaction_list(request):
    if request.user.is_superuser:
        sql = "SELECT * FROM transaction_transaction"
        with connection.cursor() as cursor:
            cursor.execute(sql)
            transactions = cursor.fetchall()
    else:
        sql = "SELECT * FROM transaction_transaction WHERE username_id = %s"
        with connection.cursor() as cursor:
            cursor.execute(sql, [request.user.id])
            transactions = cursor.fetchall()

    return render(request, "transaction_list.html", {"transactions": transactions})


@login_required
def transaction_detail(request, transaction_id):
    sql = "SELECT * FROM transaction_transaction WHERE id = %s"
    transaction = connection.cursor().execute(sql, [transaction_id]).fetchone()

    if not transaction or (
        not request.user.is_superuser and transaction["username_id"] != request.user.id
    ):
        return redirect("transaction-list")

    return render(request, "transaction_detail.html", {"transaction": transaction})

from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.db import connection


@login_required
def transaction_create(request):
    if request.method == "POST":
        try:
            Tnumber = request.POST.get("Tnumber")
            amount = request.POST.get("amount")

            # بررسی صحت داده‌ها
            if Tnumber and amount:
                # استفاده از Raw SQL برای ایجاد تراکنش
                with connection.cursor() as cursor:
                    cursor.execute(
                        """
                        INSERT INTO yourtransaction_transaction (Tnumber, username_id, amount, created_at)
                        VALUES (%s, %s, %s, NOW())
                    """,
                        [Tnumber, request.user.id, amount],
                    )

                return redirect("transaction-list")
            else:
                return HttpResponse("لطفاً تمام فیلدها را پر کنید.", status=400)
        except Exception as e:
            return HttpResponse(f"خطا: {str(e)}", status=500)

    return render(request, "transaction_form.html")
