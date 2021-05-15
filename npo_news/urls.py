from django.urls import path
from npo_news import views

urlpatterns = [
    path('api/v1/posts/', views.NewsAPIView.as_view()),
    path('api/v2/posts/', views.NewsDetailAPIView.as_view()),
]