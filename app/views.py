from django.shortcuts import redirect, render
from app.forms import AddHoodForm, NewBizForm, NewPostForm, ProfUpdateForm

from app.models import Business, Neighbourhood, Posts

# Create your views here.
def home(request):
  user_hood = request.user.profile.residence
  posts = Posts.objects.filter(residence=user_hood).all()

  # ps_form = None
  # bz_form = None
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
  if 'conts' in request.GET and request.GET["conts"]:
    contact_new = request.GET.get("conts")
    user_hood.update_neighbourhood(contact_new)

    return redirect('home')

  businesses= Business.objects.filter(residence=user_hood).all()

  #change contacts

  return render(request, "index.html", {"posts": posts, "ps_form":ps_form, "bz_form":bz_form, "businesses":businesses})

def search(request):
    if 'business' in request.GET and request.GET["business"]:
        search_term = request.GET.get("business")
        found_bz = Business.find_business(search_term)
        title = f"For {search_term}"

        return render(request, 'search.html', {"title":title, "business":found_bz})
    else:
        message = "You haven't searched for any term"
        return render(request, 'search.html',{"message":message})

def you(request):
  current_profile = request.user.profile
  businesses = Business.objects.filter(owner = current_profile).all()
  posts = Posts.objects.filter(owner = current_profile).all()
  hoods = Neighbourhood.objects.filter().all()

  # res_form = None
  # pu_form = None
  if request.method == "POST" and 'res_btn' in request.POST:
     res_form = AddHoodForm(request.POST)
     if res_form.is_valid():
        res = res_form.save(commit=False)
        res.save()
        return redirect('you')
  else:
    res_form = AddHoodForm()

  if request.method == "POST" and 'prf_btn' in request.POST:
    pu_form = ProfUpdateForm(request.POST, request.FILES,instance=request.user.profile)
    if pu_form.is_valid():
      image = pu_form.cleaned_data['pic']
      bio = pu_form.cleaned_data['about']
      current_profile.pic = image
      current_profile.about = bio
      current_profile.save()
      print("image", image)
      return redirect('you')
  else:
     pu_form =ProfUpdateForm()

  return render(request, "you.html", {"posts": posts, "businesses":businesses, "pu_form":pu_form, "res_form":res_form, "hoods":hoods, "profile":current_profile})


def bizcontacts(request, name):
      if 'bzcont' in request.GET and request.GET["bzcont"]:
        if 'desc' in request.GET and request.GET["desc"]:
          biz = Business.get(name = name)
          new_cont = request.GET.get("bzcont")
          new_description = request.GET.get("desc")
          biz.update_business(new_cont,new_description)

          return redirect('you')

def join(request, new_id, old_id):
    new_res = Neighbourhood.objects.get(id = new_id)
    user_hood = request.user.profile.residence
    old_res = None
    if old_id != None:
       old_res =  Neighbourhood.objects.get(id = old_id)

    if user_hood != new_res:
      request.user.profile.residence = new_res
      request.user.profile.save()
      new_res.census +=1
      new_res.save()
      old_res.census -= 1
      old_res.save()

    return redirect('you')

#NB add links after creating neighbourhood that lead one to the form for changing their neighbourhood
