from django.urls import path
from . import views

urlpatterns = [
    path('', views.home_view, name='home'),
    path('about-us/', views.about_us_view, name='about_us'),
    path('about-project/', views.about_project_view, name='about_project'),
]
