from django.urls import path
from . import views

urlpatterns = [

    path('', views.post_model_lis_view),
    path('<int:pk>/', views.post_model_detailed_view)
]
