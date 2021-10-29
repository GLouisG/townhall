from django.shortcuts import render

# Create your views here.
def home(request):
  val = "Welcome"
  return render(request, "index.html", {"val": val,})

#NB add links after creating neighbourhood that lead one to the form for changing their neighbourhood