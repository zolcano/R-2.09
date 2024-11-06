from django.shortcuts import render, HttpResponseRedirect
from .forms import MobileForm
from . import models


def home(request):
    Mobiles = models.Mobile.objects.all()
    return render(request, 'webapp/mobile/home.html', {'Mobile': Mobiles})

def add_Mobile(request):
    form = MobileForm()
    return render(request, 'webapp/mobile/add.html', {'form': form})

def processing(request):
    lform = MobileForm(request.POST)
    if lform.is_valid():
        lform.save()
        return render(request, 'webapp/mobile/success.html', {'Mobile': lform.cleaned_data})
    else:
        return render(request, 'webapp/mobile/error.html')

def update_Mobile(request, id):
    Mobile = models.Mobile.objects.get(id=id)
    form = MobileForm(instance=Mobile)
    return render(request, 'webapp/mobile/update.html', {'form': form, 'Mobile': Mobile})

def processing_update(request, id):
    lform = MobileForm(request.POST)
    if lform.is_valid():
        Mobile = lform.save(
            commit=False) 
        Mobile.id = id 
        Mobile.save()
        return HttpResponseRedirect("/Mobile/")
    else:
        return render(request, "webapp/Mobile/update.html", {"form": lform, "id": id})

def show_Mobile(request, id):
    Mobile = models.Mobile.objects.get(id=id)
    return render(request, 'webapp/Mobile/show.html', {'Mobile': Mobile})

def delete_Mobile(request, id):
    Mobile = models.Mobile.objects.get(id=id)
    Mobile.delete()
    return HttpResponseRedirect("/Mobile/")