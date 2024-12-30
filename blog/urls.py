from django import  urls

from . import views


urlpatterns = [
    urls.path('',views.index,name='ShopBlog'),
    urls.path('blogpost/<int:id>',views.blogpost,name='BlogPost'),
]
