from django.conf.urls import url
from django.conf.urls import url 

from checkouts import views as checkout_views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    url(r'^checkouts/$', checkout_views.new_checkout, name = 'checkouts'),
    # url(r'^payment/$', checkout_views.payment, name = 'payment'),

]
if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)

