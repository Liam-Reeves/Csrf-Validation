from django.shortcuts import render
from django import forms
from django.http import HttpResponse
from django.http import HttpResponseRedirect

# Create your views here.

class Details(forms.Form):
    name = forms.CharField(max_length=100, label="Name")
    email =forms.EmailField(max_length=100, label="Email")
    phone = forms.CharField(min_length=1, max_length=8, label="Phone")
    address = forms.CharField(max_length=100, label="Address")
    city = forms.CharField(max_length=100, label="City")
    state = forms.CharField(max_length=100, label="State")
    country = forms.CharField(max_length=100, label="Country")

 
 
def index(request):

    if request.method == "POST":
        form = Details(request.POST)
        if form.is_valid():
            print(form.cleaned_data)
            return HttpResponse("<h1>Form Submitted</h1>")
        else:
               return render(request, "index.html", {
        "form": form
    })
            
    return render(request, "index.html", {
        "form": Details()
    })
