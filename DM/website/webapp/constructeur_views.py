from django.shortcuts import render, HttpResponseRedirect
from .forms import ConstructeurForm
from . import models


def home(request):
    Constructeurs = models.Constructeur.objects.all()
    return render(request, 'webapp/Constructeur/home.html', {'Constructeur': Constructeurs})

def add_Constructeur(request):
    form = ConstructeurForm()
    return render(request, 'webapp/Constructeur/add.html', {'form': form})

def processing(request):
    lform = ConstructeurForm(request.POST)
    if lform.is_valid():
        Constructeur = lform.save()
        return render(request, 'webapp/Constructeur/success.html', {'Constructeur': Constructeur})
    else:
        return render(request, 'webapp/Constructeur/add.html', {'form': lform})

def show_Constructeur(request, id):
    Constructeur = models.Constructeur.objects.get(id=id)
    return render(request, 'webapp/Constructeur/show.html', {'Constructeur': Constructeur})

def update_Constructeur(request, id):
    Constructeur = models.Constructeur.objects.get(id=id)
    form = ConstructeurForm(instance=Constructeur)
    return render(request, 'webapp/Constructeur/update.html', {'form': form, 'Constructeur': Constructeur})

def processing_update(request, id):
    Constructeur = models.Constructeur.objects.get(id=id)
    lform = ConstructeurForm(request.POST, instance=Constructeur)
    if lform.is_valid():
        Constructeur = lform.save()
        return HttpResponseRedirect("/Constructeur/")
    else:
        return render(request, 'animeapp/Constructeur/update.html', {'form': lform, 'Constructeur': Constructeur})

def delete_Constructeur(request, id):
    Constructeur = models.Constructeur.objects.get(id=id)
    Constructeur.delete()
    return HttpResponseRedirect("/Constructeur/")