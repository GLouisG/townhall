from django.conf.urls import url
from .import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns=[
    url('^$',views.home,name='home'),
    url(r'^you/', views.you, name="you"),
    url(r'^search/',  views, name='search'),
]