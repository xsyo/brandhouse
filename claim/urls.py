from django.urls import path

from . import views


urlpatterns = [
    path('create/', views.ClaimCreateAPIView.as_view()),
    path('create/doc/', views.ClaimWithDocCreateView.as_view()),
]