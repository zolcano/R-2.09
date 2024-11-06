from django.shortcuts import render
# Create your views here.

def index(request):
    return render(request, 'myfirstapp/index.html')

def formulaire(request):
    return render(request, 'myfirstapp/formulaire.html')

def controleur(request):
    nom=request.GET["nom"]
    return render(request,'myfirstapp/controleur.html',{"nom":nom})