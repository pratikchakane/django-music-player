from django.contrib.auth.models import User
from django import forms
from django.contrib.auth.forms import UserCreationForm

from .models import Album, Song

class NewAlbum(forms.ModelForm):

    class Meta:
        model = Album
        fields = ('album_name','album_genre','album_logo',)

class SignUpForm(UserCreationForm):
    email = forms.EmailField(required='True')
    first_name = forms.CharField(required='True')
    last_name = forms.CharField(required='True')

    class meta:
        model = User
        fields = (
        'first_name',
        'last_name',
        'email',
        'username',
        'password1',
        'password2',
        )

    def save(self, commit='True'):
        user = super(SignUpForm, self).save(commit='False')
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']
        user.email = self.cleaned_data['email']


        if commit:
            user.save()
        return user

class NewSong(forms.ModelForm):

    class Meta:
        model = Song
        fields = ('song_name','song_file',)
