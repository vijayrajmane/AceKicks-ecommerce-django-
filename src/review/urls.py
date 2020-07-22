from django.urls import path

from . import views

urlpatterns = [
    path("<int:productID>", views.review, name="review"),
]