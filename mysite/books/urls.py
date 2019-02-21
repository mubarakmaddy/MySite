from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:book_id>/', views.details, name='detail'),
    path('<int:book_id>/info/', views.info, name='detail info'),
    path('<int:book_id>/info/read/', views.read, name='reading'),
]
