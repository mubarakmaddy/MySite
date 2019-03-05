from django.shortcuts import render

def home(request):

    template = 'mysite/home.html'
    return render(request, template)



