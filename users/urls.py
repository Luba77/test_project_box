from django.urls import path
from users import views


urlpatterns = [
    path('registration/', views.RegistrationCreateApiView.as_view()),
    path('authorization/', views.AuthorizationCreateApiView.as_view()),
    path('confirm/', views.ConfirmCreateApiView.as_view()),
    path('user/<int:pk>/', views.UserDetailView.as_view()),
    path('user/update/', views.UserProfileUpdateView.as_view()),
]
