from django.shortcuts import render, redirect

from .models import Entry

# Create your views here.
def index(request):
    entryid = int(request.GET.get('entryid', 0))
    query = Entry.objects.all()

    if request.method == 'POST':
        entryid = int(request.POST.get('entryid', 0))
        date = request.POST.get('date')
        header = request.POST.get('header')
        content = request.POST.get('content', '')

        if entryid > 0:
            entry = Entry.objects.get(pk=entryid)
            entry.date = date
            entry.header = header
            entry.content = content
            
            entry.save()

            return redirect('/?entryid=%i' % entryid)
        else:
            entry = Entry.objects.create(date=date, header=header, content=content)

            return redirect('/?entryid=%i' % entry.id)

    if entryid > 0:
        entry = Entry.objects.get(pk=entryid)
    else:
        entry = ''

    context = {
        'entryid': entryid,
        'entries': query,
        'entry': entry
    }
    return render(request, 'index.html', context)

def delete_entry(request, entryid):
    entry = Entry.objects.get(pk=entryid)
    entry.delete()

    return redirect('/?entryid=0')