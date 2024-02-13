from django.shortcuts import render
from django.urls import reverse
from django.http import HttpResponseRedirect
from .models import Notes

# Create your views here.
def home(request):
    all_notes = Notes.objects.all()
    return render(request, 'notes/home.html', {"all_notes": all_notes})

def add_note(request):
    if request.method == "POST":
        title = request.POST.get("title")
        content = request.POST.get("content")
        note = Notes(title=title, content=content)
        note.save()
        return HttpResponseRedirect(reverse("home"))
    return render(request, 'notes/add_note.html')

def edit_note(request, id):
    return render(request, "notes/edit_note.html")