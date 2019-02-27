from django.urls import path

from . import views

app_name = 'books'

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('<int:pk>/', views.DetailView.as_view(), name='detail'),
    # path('<int:book_id>/info/', views.info, name='detail info'),
    # path('<int:book_id>/info/read/', views.read, name='reading'),
]
