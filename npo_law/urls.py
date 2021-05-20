from django.urls import path

from npo_law import views

urlpatterns = [
    path('api/v1/law/', views.NPOLawAPIView.as_view()),
    path('api/v1/law/<int:id>/', views.NPOLawDetailAPIView.as_view()),
    path('api/v1/lawfavorite/', views.NPOLawFavoriteAPIView.as_view()),
]
