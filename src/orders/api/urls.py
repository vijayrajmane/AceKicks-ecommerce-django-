from django.urls import path
from django.views.decorators.csrf import csrf_exempt
from orders.api import views
from review.api.views import ItemReview, UserList, UserDetail, ListView

urlpatterns = [
    path('users/',UserList),
    path('users/<int:pk>/', UserDetail),

    path('product/<int:productID>/', views.Product_Detail),

    path("Statuslist/", views.StatusList),
    path("Statuslist/<int:pk>/", views.StatusDetail),
    path("changeStatus/<int:orderID>/", views.ChangeStatus),

    path("orderlist/", views.OrderList),
    path("orders/", views.myOrder),
    path("order/<int:orderID>/", views.myOrderDetail),

    path("review/<int:ID>/", ItemReview, name="productReview"),

    path("genders/", views.filterProduct, name="filterProduct"),

    path("gender/<int:genID>/", views.genderShoe, name="genderShoe_api"),
    path("brand/<int:brandID>/", views.brandShoe, name="brandShoe_api"),
    path("category/<int:catID>/", views.categoryShoe, name="categoryShoe_api"),

    path("detail/<int:productID>/", views.detailPage, name="categoryShoe_api"),

    path('cart/', views.cart, name="cart_api"),
    path('cart/<int:rowID>/', views.cartDetail, name="cartDetail_api"),

    path('confirm/', views.ConfirmOrder),
    path('confirm/detail/', views.ConfirmOrderDetail),
]
