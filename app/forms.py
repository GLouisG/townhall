from django import forms

from app.models import Profile, Posts, Business, Neighbourhood
class AddHoodForm(forms.ModelForm):
    class Meta:
      model = Neighbourhood
      exclude=["census"]
class NewPostForm(forms.ModelForm):
    class  Meta:
      model = Posts
      exclude = ['owner', 'residence']
class ProfUpdateForm(forms.ModelForm):
    class Meta:
      model = Profile
      fields = ('about', 'pic')      
class NewBizForm(forms.ModelForm):
    class Meta:
      model = Business
      exclude=["residence", "owner"]