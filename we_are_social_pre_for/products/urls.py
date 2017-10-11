from django.conf.urls import url
import views as product_views

urlpatterns = [
    url(r'^products/$', product_views.all_products),
]