from django import forms
from .models import RedTasting

class RedTastingForm(forms.ModelForm):
    
    class Meta:
        model = RedTasting
        fields = ('coolness','shine','tone','shade','viscosity','freshhness','Maturity')
        widgets = { 'coolness': forms.RadioSelect(),
                    'shine': forms.RadioSelect(),
                    'tone': forms.RadioSelect(),
                    'shade': forms.RadioSelect(),
                    'viscosity': forms.RadioSelect(),
                    'freshhness': forms.RadioSelect(),
                    'Maturity': forms.RadioSelect(),
                    }
        