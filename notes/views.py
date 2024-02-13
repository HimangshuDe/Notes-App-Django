from django.shortcuts import render
from django.http import HttpResponse
from .models import Notes

# Create your views here.
def home(request):
    all_notes = Notes.objects.all()
    return render(request, 'notes/home.html', {"all_notes": all_notes})

def add_note(request):
    # return HttpResponse("Add Note Page")
    return render(request, 'notes/add_note.html')

def edit_note(request, id):
    return HttpResponse("Edit Note Page")