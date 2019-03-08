from django.urls import path
from .views import (
    BookCreate,
    IndexView,
    BookDetailView,
    BookUpdate,
    DeleteView,
)


app_name = 'books'

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('<int:pk>/', BookDetailView.as_view(), name='detail'),
    path('add/', BookCreate.as_view(), name='add-book'),
    path('<int:pk>/update/', BookUpdate.as_view(), name='update-book'),
    path('<int:pk>/delete/', DeleteView.as_view(), name='delete-book'),

]
