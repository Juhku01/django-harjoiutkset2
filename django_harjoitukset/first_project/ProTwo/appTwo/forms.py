from django import forms
from appTwo.models import User
#4 rivi ei toimi
class NewUserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = '__all__'
