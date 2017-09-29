from django.conf.urls import url
import views as magazine_views

urlpatterns = [
    url(r'^magazines/$', magazine_views.all_magazines),
]
