from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from apps.accounts.forms import UserLoginForm, CreateUserForm
from django.contrib import messages


def register_page(request):
    form = CreateUserForm()

    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            user = form.cleaned_data.get('username')
            messages.success(request, 'Conta foi criada com sucesso para ' + user)

            return redirect('login')

    context = {'form': form}
    return render(request, 'registration/register.html', context)


def login_view(request):
    form = UserLoginForm(request.POST or None)
    if form.is_valid():
        username = form.cleaned_data.get("username")
        password = form.cleaned_data.get("password")
        user = authenticate(username=username, password=password)
        login(request, user)
        return redirect('/')
    return render(request, 'registration/login.html', {'form': form})


def logout_view(request):
    logout(request)
    return render(request, 'registration/logout.html', {})
