from django.shortcuts import render
from data import NOTES

# Create your views here.
def notes_view(request):
    return render(request, 'notes/notes_list.html', {
        'notes': NOTES,
    })

def notes_detail(request, id):
    notes_list = NOTES[id]
    return render(request, 'notes/notes_detail.html', {
        'notes_list': notes_list,
    })