from django.urls import path

from . import views

urlpatterns = [

        path("logout", views.logout_view, name="logout"),
        path("rregister", views.userRegister, name="register"),
        path("login", views.login_view, name="login"),
        path("checkout", views.checkoutPage, name="checkout"),
        path("myorder/", views.myOrders, name="myorders"),
        path("manageOrder/", views.manageOrder, name="manageOrder"),
        path("detail/<int:productID>/", views.detailPage, name="detail_view"),
        path("cart/", views.cartPage, name="cart"),
        path("gender/<int:genID>/", views.genderShoe, name="gender_view"),
        path("brand/<int:brandID>/", views.brandShoe, name="brand_view"),
        path("category/<int:catID>/", views.categoryShoe, name="category_view"),
        path("", views.index, name="index"),
]
