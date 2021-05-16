from django import forms
from .models import Message, Dogs, Req
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class messageform(forms.ModelForm):
    class Meta:
        model=Message
        fields=("name","email","subject","message")
class NewUserForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ("username", "email", "password1", "password2")

    def save(self, commit=True):
        user = super(NewUserForm, self).save(commit=False)
        user.email = self.cleaned_data["email"]
        if commit:
            user.save()
        return user
class Sellform(forms.ModelForm):
    class Meta:
        model=Dogs
        fields=["image","breed","description","phone_number","location"]
class Reqform(forms.ModelForm):
    class Meta:
        model=Req
        fields=['name','need','phone_number']