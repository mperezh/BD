### home/urls.py ###

from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', view=views.index, name='home'),
    url(r'^home/$', view=views.index, name='home'),
    url(regex=r'^about/$', view=views.AboutView.as_view(), name='about'),
    url(regex=r'^trainers/$', view=views.TrainersView.as_view(), name='trainers'),
    url(regex=r'^contact/$', view=views.ContactView.as_view(), name='contact'),
]
