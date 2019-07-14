from django.shortcuts import render
from django.http import HttpResponse
from accounts.forms import UserForm

def home(request):
    if request.user.is_authenticated:
        print(request.user.profile.city)
    return HttpResponse("ok")

def register(request):

    form = UserForm(request.POST or None)
    if form.is_valid():
        user = form.save() # Save in database
        # user.refresh_from_db()
        user.profile.city = form.cleaned_data.get('city')
        user.save()
        
        form = UserForm()
    return render(request,'registration.html', {'user_form':form})
