from django.urls import path
from blog import views
urlpatterns = [
    path("" , views.homepage , name="home-page")  ,  #path for starting page 
    path("posts" , views.posts , name="posts-page"),   #load page with all blog post
    path("posts/<slug:slug>" , views.post_details , name="posts-details-page")   #path of a specific full blog post dynamic - posts/(my-first-post)-->"this part is known as slug"/ 
]
