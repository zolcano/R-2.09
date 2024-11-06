from django.forms import ModelForm
from django.utils.translation import gettext_lazy as _
from . import models


class MobileForm(ModelForm):

    class Meta:
        model =models.Mobile
        fields = ('nom', 'date_parution', 'prix', 'constructeur')
        labels = {
            'nom': _('Nom'),
            'date_parution': _('Date'),
            'prix': _('Prix'),
            'constructeur': _('Constructeur'),
        }

class ConstructeurForm(ModelForm):

    class Meta:
        model = models.Constructeur
        fields = ('marque', 'pays')
        labels = {
            'marque': _('Marque'),
            'pays': _('Pays'),
        }