from django.urls import path
from django.contrib.auth import views as auth_views
from . import views
urlpatterns = [
    path("", views.index, name="index"),
    path("post-detail/<slug:slug>", views.post_detail, name="post-detail"),
    path("add-new-post", views.add_new_post, name="add-new-post"),
    path("edit-post/<slug:slug>", views.edit_post, name="edit-post"),
    path("delete-post/<slug:slug>", views.delete_post, name="delete-post"),
    path("register", views.register, name="register"),
    path("login", auth_views.LoginView.as_view(
        template_name="crudApp/login.html"), name="login"),
    path("logout", auth_views.LogoutView.as_view(), name="logout"),
    path("dashboard", views.dashboard, name="dashboard"),

    path("test_data/<int:id>", views.test_data, name="test_data"),

    path("profile/<int:id>", views.profile, name="profile"),
    path("search_posts", views.search_posts, name="search_posts"),
    path("comments/<int:id>", views.comments, name="comments")
]
