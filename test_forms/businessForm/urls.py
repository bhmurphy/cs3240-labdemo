from django.conf.urls import url

from . import views


urlpatterns = [

]

urlpatterns += [   
    url(r'^businessForm/$', views.business_form),
]
