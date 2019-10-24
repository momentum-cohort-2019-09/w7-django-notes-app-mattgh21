from django.shortcuts import render, redirect, get_object_or_404
from notes.models import Note
from django.views.generic.edit import FormView
from django.utils import timezone
from django.http import HttpResponse
from .forms import NoteForm


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
        form = NoteForm(request.POST)
        if form.is_valid():
            note = form.save(commit=False)
            note.created_at = timezone.now()
            note.save()
            return redirect('/') 
    else:
        form = NoteForm()
    return render(request, 'notes/add_note.html', {
        'form': form
    })
    
def edit_note(request):
    note = get_object_or_404(Note, ide=pk)
    if request.method == "POST":
        form = NoteForm(request.POST, instance=note)
        if form.is_valid():
            note = form.save(commit=False)
            note.updated_at = timezone.now()
            note.save()
            return redirect('/')
    else:
        form = NoteForm()
    return render(request, 'notes/edit_note.html',{
        'form': form
    })
