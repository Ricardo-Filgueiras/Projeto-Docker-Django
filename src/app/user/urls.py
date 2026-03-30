from django.urls import path
from django.contrib.auth import views as auth_views
from . import views
from .forms import SecureLoginForm

app_name = 'user'

urlpatterns = [
    path('', views.user_index, name='user_index'),

    path('register/', views.register, name='register'),
    path('login/', auth_views.LoginView.as_view(
        template_name='user/login.html',
        authentication_form=SecureLoginForm
    ), name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='user:index'), name='logout'),
    path('profile/', views.profile, name='profile'),
    path('profile/update/', views.profile_update, name='profile_update'),
    path('profile/delete/', views.account_delete, name='account_delete'),
]