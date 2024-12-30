from django import urls
from . import views

urlpatterns = [
    urls.path("", views.index, name="index"),
    urls.path("about/",views.about,name="about"), 
    urls.path("contact/",views.contact,name="contact"),
    urls.path("tracker/",views.tracker,name="tracker"),
    urls.path("product/<int:myid>",views.productView,name="productView"),
    urls.path("checkout/",views.checkout,name="checkout"),    
    urls.path("search/",views.search,name="search"),
    urls.path("handlerequest",views.handlerequest,name="handlerequest"),
]
