from django.urls import path
from . import views


urlpatterns = [
    path('', views.HomeView.as_view(), name='home'),
    path('about/', views.AboutView.as_view(), name='about'),
    path('posts/<int:pk>', views.PostView.as_view(), name='post-detail'),
    path('contact/', views.ContactView.as_view(), name='contact')
]
