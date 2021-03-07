from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("login/", views.login_view, name="login"),
    path("logout", views.logout_view, name="logout"),
    path("register", views.register, name="register"),
    path("listing/<str:listingid>", views.listingpage, name="listingpage"),
    path("category", views.categoryindex, name="categoryindex"),
    path("category/<str:categoryid>", views.categorypage, name="categorypage"),
    path("create", views.create, name="create"),
    path("comment", views.comment, name="comment"),
    path("bid", views.bid, name="bid"),
    path("watchlist/<str:userid>", views.watchlist, name="watchlist"),
    path("unsave", views.unsave, name="unsave"),
    path("inactive", views.inactive, name="inactive"),
    path("all", views.all, name="all")
]
