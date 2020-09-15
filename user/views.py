from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth
from django.contrib import messages
from calcu import views
# Create your views here.


def logout(request):
    auth.logout(request)
    return redirect('home')


def main(request):
    if(request.method == "GET"):
        return render(request, 'index.html')
    else:
        num1 = request.POST['first']
        num2 = request.POST['second']
        p = request.POST['operator']

        def switch(p, num1, num2):

            if p == '+':
                result = int(num1)+int(num2)
                return result

            elif p == '-':
                result = int(num1)-int(num2)
                return result

            elif p == '*':
                result = int(num1)*int(num2)
                return result

            elif p == '/':
                result = int(num1)/int(num2)
                return result

            else:
                result = int(num1) % int(num2)
                return result

        result = switch(p, num1, num2)
        return render(request, 'result.html', {'r': result})


def login(request):
    if(request.method == "GET"):
        return render(request, 'login.html')
    else:
        password = request.POST['password']
        username = request.POST['username']
        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect('main')
        else:

            messages.info(request, 'Invalid credentials')
            return redirect('login')


def register(request):
    if(request.method == "GET"):
        return render(request, 'register.html')
    else:
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        email = request.POST['email']
        password = request.POST['password']
        username = request.POST['username']
        if User.objects.filter(username=username).exists():
            messages.info(request, 'Username already exists ! Try another one')
            return redirect('register')
        elif User.objects.filter(email=email).exists():
            messages.info(request, 'Email already exists ! Try another one')
            return redirect('register')

        else:
            user = User.objects.create_user(
                username=username, email=email, password=password, first_name=first_name, last_name=last_name)

            user.save()
            return redirect('/')
