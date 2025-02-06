from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth.models import User

def auth(request):
    if request.user.is_authenticated:
        return redirect('/') 

    if request.method == 'POST':
        email = request.POST.get('email')
        try:
            user = User.objects.get(email=email)
            login(request, user)
            return redirect('/')  
        except User.DoesNotExist:
            return render(request, 'login.html', {'error': 'User with this email does not exist.'})

    return render(request, 'login.html')
