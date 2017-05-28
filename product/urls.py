from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
from product import views

urlpatterns = [
    url(r'^$', views.ProductList.as_view()),
    url(r'^$', views.ProductDetail.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)
