from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.contrib.auth import login, logout, authenticate

# Create your views here.



@api_view(["POST"])    
def signup(req):
    error = False
    if req.method == 'POST':
        form = SignupForm(req.POST)
        if form.is_valid():
            first_name = form.cleaned_data['first_name']
            last_name = form.cleaned_data['last_name']
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            
            try:
                User.objects.create_user(first_name=first_name, last_name=last_name, username=email, email=email, password=password)
                return HttpResponseRedirect("/")
            except:
                error = True
                pass
        else:
            pass
            

    return  render(req, "blog/signup.html", {
        "form": form,
        "hasError": error
    })
    
    
@api_view(["POST"])    
def login_view(req):     
    try:    
        email = req.body.email
        password = req.body.password    
        user = authenticate(username=email, password=password)
        print(user)
        if user == None:
            return render(req, "blog/login.html", {
                "form": form,
                "error": "Wrong Email or Password"
            })
        else:
            login(req, user)
    except:
        return render(req, "blog/login.html", {
            "form": form,
            "error": "Wrong Email or Password"
        })
                
    return render(req, "blog/login.html", {
        "form": form,
    })

@api_view(["GET"])    
def logout_view(req): 
    logout(req)
    return HttpResponseRedirect("/")
