from django.urls import path
from . import views


app_name = 'jobs'
urlpatterns = [

    path('', views.post_new_job, name='jobs-home'),
]
