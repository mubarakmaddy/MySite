from django.urls import path
from django.contrib.auth import views as auth_views
from . import views
app_name = 'signup'
urlpatterns = [

    path('signup/', views.register, name='myapp-signup'),
    path('signupsuccess/', views.register_successfull, name='signup-success'),
    path('login/', auth_views.LoginView.as_view(template_name='users/login.html'), name='myapp-login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='users/logout.html'), name='myapp-logout')

]
