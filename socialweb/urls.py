from django.urls import path
from socialweb.views import SignupView,SigninView,IndexView,add_comments,comment_like,signout_view,post_delete_view,PostAddView,comment_delete_view

urlpatterns = [
    path("register",SignupView.as_view(),name="signup"),
    path("login",SigninView.as_view(),name="signin"),
    path(" ",IndexView.as_view(),name="index"),
     path("posts/add",PostAddView.as_view(),name="post-add"),
    path("posts/<int:id>/remove",post_delete_view,name="post-delete"),
   path("posts/<int:id>/comments/add",add_comments,name="add-comment"),
   path("comments/<int:id>/like/add",comment_like,name="comment-like"),
   path("comments/<int:id>/remove",comment_delete_view,name="comment-delete"),

   path("logout",signout_view,name="signout")
]
