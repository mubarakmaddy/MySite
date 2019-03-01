from django.http import HttpResponse


def home(request):
    return HttpResponse("<h1>Hello World</h1>")


def emp(request):
    return HttpResponse("hsdj")


class Home():
    def as_view(request):
        return HttpResponse("<h1>Hello World</h1>")


