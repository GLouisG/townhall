from django.conf.urls import url
from .import views
from django.conf.urls.static import static
from django.conf import settings
from django.urls import path

urlpatterns=[
    url('^$',views.home,name='home'),
    url(r'^you/', views.you, name="you"),
    url(r'^search/',  views.search, name='search'),
    path("bizcontacts/<str:name>/",views.bizcontacts, name="bizcontacts"),    
    path("join/<int:new_id>/<int:old_id>",views.join, name="join"),
]