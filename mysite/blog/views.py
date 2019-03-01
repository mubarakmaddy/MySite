from django.shortcuts import render

from .models import PostModel


def post_model_lis_view(request):
    qs = PostModel.objects.all()
    # print(request.user.is_authenticated)
    context = {

        "object_list": qs
    }

    template = "blog/list-view.html"

    return render(request, template, context)

def post_model_detailed_view(request):

    qs = PostModel.objects.all()
    context = {


    }
    template = "blog/detailed-view.html"

    return render(request, template, context)
