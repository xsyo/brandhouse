from django.urls import path

from . import views

urlpatterns = [
    path('claims/', views.ClaimListAPIView.as_view()),
    path('claims/<int:pk>', views.ClaimRetrieveUpdateAPIView.as_view()),
    path('claims/<int:claim_id>/answer', views.reply_to_application),
    path('claims/<int:claim_id>/account-create', views.ClientCreateAPIView.as_view()),

    path('<int:pk>/', views.ManagerRetrieveUpdateAPIView.as_view()),

    
    path('', views.ManagerListCreateAPIView.as_view()), # Для админа
]