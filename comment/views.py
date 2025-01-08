from django.shortcuts import render, redirect
from .models import Poll, Poll_comment


def poll_list(request):
    with connection.cursor() as cursor:
        cursor.execute("SELECT * FROM poll_poll")
        polls = cursor.fetchall()
    
    return render(request, 'poll_list.html', {'polls': polls})

def poll_detail(request, poll_id):
    with connection.cursor() as cursor:
        cursor.execute("SELECT * FROM poll_poll WHERE id = %s", [poll_id])
        poll = cursor.fetchone()
    
    if poll is None:
        return redirect('poll-list')  # اگر نظرسنجی پیدا نشد، برگشت به لیست
    return render(request, 'poll_detail.htm', {'poll': poll})


def poll_created(request):
    if request.method == 'POST':
        text = request.POST.get('text')
        if text:
            with connection.cursor() as cursor:
                cursor.execute("""
                    INSERT INTO poll_poll (text, created_at, updated_at)
                    VALUES (%s, NOW(), NOW())
                """, [text])
            return redirect('poll-list')
    
    return render(request, 'poll_form.html')

    
def poll_delete(request, poll_id):
    with connection.cursor() as cursor:
        cursor.execute("DELETE FROM poll_poll WHERE id = %s", [poll_id])
    return redirect('poll-list')
