from django import forms
from .models import Message, UserBlog
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
class blogform(forms.ModelForm):
    class Meta:
        model=UserBlog
        fields=("title","description","stitle","content","stitle1","content1","stitle2","content2","stitle3","content3")