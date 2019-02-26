from django.urls import path

from . import views

app_name = 'books'

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:book_id>/', views.details, name='detail'),
    path('<int:book_id>/info/', views.info, name='detail info'),
    path('<int:book_id>/info/read/', views.read, name='reading'),
]
