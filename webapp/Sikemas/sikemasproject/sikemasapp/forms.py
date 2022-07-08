from django import forms
from .models import Opd
 
 
# creating a form
class FormOPD(forms.ModelForm):

    # create meta class
    class Meta:
        # specify model to be used
        model = Opd

        # specify fields to be used
        fields = '__all__'
