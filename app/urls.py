from django.conf.urls import url
from .import views
from django.conf.urls.static import static
from django.conf import settings
from django.urls import path

urlpatterns=[
    url(r'^home/',views.home,name='home'),
    url(r'^$', views.you, name="you"),
    url(r'^search/',  views.search, name='search'),
    path("bizcontacts/<str:name>/",views.bizcontacts, name="bizcontacts"),    
    path("join/<int:new_id>/<int:old_id>",views.join, name="join"),
    path("join/<int:new_id>/",views.join, name="join"),    
]
if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)