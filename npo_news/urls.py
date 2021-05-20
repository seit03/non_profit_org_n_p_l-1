from django.urls import path
from npo_news import views

urlpatterns = [
    path('api/v1/news/', views.NewsAPIView.as_view()),
    path('api/v2/news/<int:id>/', views.NewsDetailAPIView.as_view()),
    path('api/v1/news/', views.NewsFavoriteAPIView.as_view()),
]