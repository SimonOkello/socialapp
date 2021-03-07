from django import forms
from django.forms import fields

from .models import Profile


class ProfileModelForm(forms.ModelForm):
    bio = forms.CharField(widget=forms.Textarea(attrs={'rows':2}))
    class Meta:
        model = Profile
        fields = ('first_name', 'last_name', 'bio', 'avatar',)
