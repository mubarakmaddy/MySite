from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.urls import reverse


def register(request):

    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Welcome {username}! ')
            return redirect('signup:signup-success')

    else:
        form = UserCreationForm()
    context = {
        'form': form
    }
    template = 'users/register.html'
    return render(request, template, context)



def register_successfull(request):

    template = 'users/register-success.html'

    return render(request, template)
