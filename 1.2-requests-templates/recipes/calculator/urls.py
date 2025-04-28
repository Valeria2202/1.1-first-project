from django.urls import path
from . import views
from django.shortcuts import redirect

def redirect_to_omlet(request):
    return redirect('recipe', dish='omlet')

urlpatterns = [
    path('<str:dish>/', views.recipe, name='recipe'),
    path('', redirect_to_omlet, name='home'),
]