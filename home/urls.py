from django.conf.urls import url
from django.conf.urls import url 

from home import views as home_views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    url(r'^$', home_views.home, name = 'home'),

]
if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)

