from django.shortcuts import redirect, render
from app.forms import AddHoodForm, NewBizForm, NewPostForm, ProfUpdateForm

from app.models import Business, Neighbourhood, Posts

# Create your views here.
def home(request):
  user_hood = request.user.profile.residence 
  posts = Posts.objects.filter(residence=user_hood).all()
  
  if request.method == "POST" and 'ps_btn' in request.POST:
     ps_form = NewPostForm(request.POST) 
     if ps_form.is_valid():
        post = ps_form.save(commit=False)
        post.owner = request.user.profile
        post.residence = user_hood
        post.save()
        return redirect('home')
     else:
       ps_form = NewPostForm()     

  if request.method == "POST" and 'bz_btn' in request.POST:
     bz_form = NewBizForm(request.POST) 
     if bz_form.is_valid():
        biz = bz_form.save(commit=False)
        biz.owner = request.user.profile
        biz.residence = user_hood
        biz.save()
        return redirect('home')
     else:
       bz_form = NewBizForm()