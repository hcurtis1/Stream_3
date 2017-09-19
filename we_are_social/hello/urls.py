from django.conf.urls import url
import views as hello_views

urlpatterns = [
    url('^$', hello_views.get_index),
]
