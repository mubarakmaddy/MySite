from django.urls import path
from . import views

app_name = "blog"

urlpatterns = [

    # path('', views.post_model_lis_view),
    # path('<int:pk>/', views.post_model_detailed_view),
    # path('create', views.post_model_create_view)
    path('', views.home, name='blog-home'),

]
