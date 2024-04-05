from django.shortcuts import render, redirect
from .forms import RegisterForm

# Overriding default registration view
def signup(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = RegisterForm()

    return render(request, "registration/signup.html", {'form':form})