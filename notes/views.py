from django.shortcuts import render
from notes.models import Note, NoteForm
from django.views.generic.edit import FormView


# Create your views here.
def notes_list(request):
    notes = Note.objects.all()
    return render(request, 'notes/notes_list.html', {
        'notes': notes,
    })

def notes_detail(request, pk):
    note = Note.objects.get(id=pk)
    return render(request, 'notes/notes_detail.html', {
        'note': note,
    })

def add_note(request):
    if request.method == 'POST':
        pass
    else:
        return render(request, 'notes/add_note.html')
    