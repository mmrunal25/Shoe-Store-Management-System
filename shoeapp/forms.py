#from typing import Any, Mapping
#from django.core.files.base import File
#from django.db.models.base import Model
#from django.forms.utils import ErrorList
from .models import Shoe
from django import forms
#from .models import Shoe, CustomUser
from django.contrib.auth.forms import UserCreationForm

class SignUpForm(UserCreationForm):
    city = forms.CharField(max_length=50)
    phone_number = forms.CharField(max_length=20)

    class Meta:
        #model = User
        fields =  ['first_name', 'last_name', 'username', 'email', 'city', 'phone_number']

        def save(self, commit=True):
            user = super().save(commit=False)
            user.city = self.cleaned_data['city']
            user.phone_number = self.cleaned_data['phone_number']

            if commit:
                user.save()
            return user

class ShoeForm(forms.ModelForm):
    class Meta :
        model = Shoe
        fields = ['id','brand','price','size','color', 'product_image']

        widget={
            'id' : forms.NumberInput(attrs={'class':'form-control'}),
            'brand' : forms.TextInput(attrs={'class':'form-control'}),
            'price' : forms.NumberInput(attrs={'class':'form-control'}),
            'size' : forms.NumberInput(attrs={'class':'form-control'}),
            'color' : forms.TextInput(attrs={'class':'form-control'}),
            'product_image' : forms.TextInput(attrs={'class':'form-group-file'}),
        }
    
    
    
    
    
    '''def __init__(self, *args, **kwargs):
        super().__init__( *args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs.update('class' : 'form-group')'''