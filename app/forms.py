from django import forms

from app.models import Profile, Post, Business, Neighbourhood
class AddHoodForm(forms.ModelForm):
    class Meta:
      model = Neighbourhood
      exclude=["census"]
class NewPostForm(forms.ModelForm):
    class  Meta:
      model = Post
      exclude = ['owner', 'residence']
class ProfUpdateForm(forms.ModelForm):
    class Meta:
      model = Profile
      fields = ('about', 'pic')      
