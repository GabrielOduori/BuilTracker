from django.conf.urls import url
from .views import views,financier,owner

urlpatterns=[
    url('',views.index,name='index'),
    url('',views.create_wallet,name='create_wallet'),
    url('',views.view_wallet,name='view_wallet'),
]