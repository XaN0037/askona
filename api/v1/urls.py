from django.urls import path
from api.v1.auth.users import UserView
from api.v1.auth.views import AuthView
from api.v1.basket.views import BasketView
from api.v1.category.views import CategoryView
from api.v1.comment.views import CommentView, Comments
from api.v1.discount.views import DiscountView
from api.v1.filter.views import SearchView, Filteratsiya, CustomFilter
from api.v1.product.views import ProductView
from api.v1.saved_product.views import ProsavedView
from api.v1.sub_category.views import SubcategoryView
from api.v1.tkan.views import PartnersView

urlpatterns = [
    path("auth/", AuthView.as_view()),
    path("user/", UserView.as_view()),

    path("basket/", BasketView.as_view()),
    path("prosaved/", ProsavedView.as_view()),

    path("comment/", CommentView.as_view()),
    path("comment/<int:pk>/", Comments.as_view()),

    path("category/", CategoryView.as_view()),
    path("category/<int:pk>/", CategoryView.as_view()),

    path("subcategory/<int:pk>/", SubcategoryView.as_view()),
    path("subcategory/", SubcategoryView.as_view()),

    path("discount/<int:pk>/", DiscountView.as_view()),
    path("discount/", DiscountView.as_view()),

    path("product/", ProductView.as_view()),
    path("product/<int:pk>/", ProductView.as_view()),

    path("search/", SearchView.as_view()),
    path("filter/", Filteratsiya.as_view()),

    path('tkan/', PartnersView.as_view()),
    path('p-fil/', CustomFilter.as_view()),

]
