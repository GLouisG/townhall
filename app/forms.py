from django import forms

from app.models import Profile, Post, Business, Neighbourhood
class AddHoodForm(forms.ModelForm):
    class Meta:
      model = Neighbourhood
      exclude=["census"]

