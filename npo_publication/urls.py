from django.urls import path

from npo_publication import views

urlpatterns = [
    path('api/v1/publication/', views.PublicationAPIView.as_view()),
    path('api/v1/publication/<int:id>/', views.PublicationDetailAPIView.as_view()),
    path('api/v1/publication/', views.PublicationFavoriteAPIView.as_view()),
]