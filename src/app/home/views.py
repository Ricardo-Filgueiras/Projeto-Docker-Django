from django.shortcuts import render

# Create your views here.
# urlpatterns = [
#     path('', views.index, name='index'),
#     path('home/', views.index, name='index'),
# ] 

def index(request):
    return render(request, 'index.html')
