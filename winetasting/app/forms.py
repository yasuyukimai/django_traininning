from django import forms
from .models import RedTasting

class RedTastingForm(forms.ModelForm):
    
    class Meta:
        model = RedTasting
        fields = ('grape','country','coolness','shine','tone','shade','viscosity','freshhness','Maturity')
        
        