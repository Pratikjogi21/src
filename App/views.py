from django.shortcuts import render,redirect
from .models import Note

def home(request):
    notes = Note.objects.all()
    return render (request,'home.html',{"notes":notes})

def add(request):
    if(request.method=="POST"):
        nt = request.POST.get("title")
        nd = request.POST.get("description")
        note = Note()
        note.notetitle = nt
        note.notedescr = nd
        note.save()
        return redirect("/")
    else:  
        return render(request,'add.html')
    
def delete(request,id):
    note = Note.objects.get(id=id)
    if(note):
        note.delete()
    return redirect('/')


def viewone(request,id):
    note = Note.objects.get(id=id)
    return render(request,"viewone.html",{"m":note})

def edit(request,id):
    note = Note.objects.get(id=id)
    if(request.method=="POST"):
        nt = request.POST.get("title")
        nd = request.POST.get("description")
        note.notetitle = nt
        note.notedescr = nd
        note.save()
        return redirect("/")
    else:
        return render(request,"edit.html",{'m':note})

