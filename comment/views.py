from django.shortcuts import render, get_object_or_404, redirect
from .models import Poll, Poll_comment
from .forms import PollForm

def poll_list(request):
    polls = Poll.objects.all()
    return render(request, 'poll_list.html', {'polls' : polls})

def poll_detail(request, poll_id):
    poll = get_object_or_404(Poll, id=poll_id)
    return render(request, 'poll_detail.htm', {'poll': poll})


def poll_created(request):
    if request.method == 'POST':
        form = PollForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('poll-list')
    form = PollForm()
    return render(request, 'poll_form.html', {'form' : form})
    
def poll_delete(request, poll_id):
    poll = get_object_or_404(Poll, id=poll_id)
    poll.delete()
    return redirect('poll-list')
