from django.shortcuts import render, redirect, get_object_or_404
from notes.models import Note
from django.views.generic.edit import FormView
from django.utils import timezone
from django.http import HttpResponse
from .forms import NoteForm, SearchForm, SortForm


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
    
def edit_note(request, pk):
    note = get_object_or_404(Note, id=pk)
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

def delete_note(request, pk):
    Note.objects.get(id=pk).delete()
    return redirect('/')

def search_notes(request):
    selected_notes = []
    if request.method == 'POST':
        form = SearchForm(request.POST)
        if form.is_valid():
            notes = Note.objects.all()
            data = request.POST.copy()
            for note in notes:
                if data.get('search_text').casefold() in note.title.casefold():
                    selected_notes.append(note)
            return render(request, 'notes/searched_notes.html',{
                'notes': selected_notes})
        
    else:
        form = SearchForm()
        return render(request, 'notes/search_notes.html',{
            'form': form})

def sort_notes(request):
    if request.method == 'POST':
        form = SortForm(request.POST)
        if form.is_valid():
            data = request.POST.copy()
            if data.get('by_title'):
                if data.get('asc_or_desc') == 'Descending':
                    sorted_notes = Note.objects.order_by('-updated_at', 'title')
                elif data.get('asc_or_desc') == 'Ascending':
                    sorted_notes = Note.objects.order_by('-updated_at', 'title')
                elif data.get('asc_or_desc') == 'Neither':
                    sorted_notes = Note.objects.order_by('title')
            else:
                if data.get('asc_or_desc') == 'Descending':
                    sorted_notes = Note.objects.order_by('-updated_at')
                elif data.get('asc_or_desc') == 'Ascending':
                    sorted_notes = Note.objects.order_by('-updated_at')
        return render(request, 'notes/sorted_notes.html',{
            'notes': sorted_notes
        })

    else:
        form = SortForm()
    return render(request, 'notes/sort_notes.html',{
        'form': form
    })
                    