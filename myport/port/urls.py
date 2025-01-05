from django.urls import path
from port import views

app_name="port"

urlpatterns = [
    path("",views.home,name='home'),
    path("index",views.home,name='home'),
    path("about",views.about,name='about'),
    path("blogs",views.get_Blog,name='blog'),
    path("contact",views.get_contact,name='contact'),
    path("resume",views.get_resume,name='resume'),
    path("<int:id>",views.get_blogArticle,name='get_blogArticle'),   
    # path("articles/by/category/<int:id>/",views.get_articlesbycategory,name='articlesbycategory'),
    # path("article/detail/<int:id>/",views.get_article,name='get_article'),

] 