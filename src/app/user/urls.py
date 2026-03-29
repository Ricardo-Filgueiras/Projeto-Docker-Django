from django.urls import path

app_name = 'user'

urlpatterns = [
    path('profile/', views.profile, name='profile'),
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
    path('register/', views.register, name='register'),
    path('update/', views.update, name='update'),
]   