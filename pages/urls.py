from django.urls import path
from . import views


urlpatterns = [
    path('', views.HomeView.as_view(), name='home'),
    path('about/', views.AboutView.as_view(), name='about'),
    path('posts/<int:pk>', views.PostView.as_view(), name='post-detail'),
    path('contact/', views.ContactView.as_view(), name='contact'),
    path('create/', views.PostCreateView.as_view(), name='post_create'),
    path('edit/<int:pk>', views.PostEditView.as_view(), name='post_edit'),
    path('delete/<int:pk>', views.PostDeleteView.as_view(), name='post_delete')
]
