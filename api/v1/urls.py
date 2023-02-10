from django.urls import path
from api.v1.auth.users import UserView
from api.v1.auth.views import AuthView
from api.v1.basket.views import BasketView
from api.v1.saved_product.views import ProsavedView

urlpatterns = [
    path("auth/", AuthView.as_view()),
    path("user/", UserView.as_view()),
    path("basket/", BasketView.as_view()),
    path("prosaved/", ProsavedView.as_view()),
]
