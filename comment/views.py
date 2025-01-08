from django.shortcuts import render, get_object_or_404, redirect
from django.db import connection

def poll_list(request):
    with connection.cursor() as cursor:
        cursor.execute(
            "SELECT * FROM comment_poll"
        )  # در اینجا 'comment_poll' نام جدول Poll است
        polls = cursor.fetchall()
    return render(request, "poll_list.html", {"polls": polls})


def poll_detail(request, poll_id):
    with connection.cursor() as cursor:
        cursor.execute("SELECT * FROM comment_poll WHERE id = %s", [poll_id])
        poll = cursor.fetchone()
    if poll:
        return render(request, "poll_detail.htm", {"poll": poll})
    else:
        return redirect("poll-list")


def poll_created(request):
    if request.method == "POST":
        title = request.POST.get("title")  # فرض می‌کنیم که فرم فیلدی به نام title دارد
        description = request.POST.get(
            "description"
        )  # فرض می‌کنیم که فرم فیلدی به نام description دارد
        with connection.cursor() as cursor:
            cursor.execute(
                "INSERT INTO comment_poll (title, description, created_at) VALUES (%s, %s, NOW())",
                [title, description],
            )
        return redirect("poll-list")
    return render(request, "poll_form.html")


def poll_delete(request, poll_id):
    with connection.cursor() as cursor:
        cursor.execute("DELETE FROM comment_poll WHERE id = %s", [poll_id])
    return redirect("poll-list")
