from django.urls import path
from api.v1.auth.users import UserView, Logout, ChangePasswordView
from api.v1.auth.views import AuthView

urlpatterns = [
    path("auth/", AuthView.as_view()),
    path("user/", UserView.as_view()),
    path("user/<int:pk>/", UserView.as_view()),
    path("user/logout/", Logout.as_view()),
    path('user/changpass/<int:pk>/', ChangePasswordView.as_view()),
]
