from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.rubrica_list, name='rubrica_list'),
	url(r'^nomi/(?P<pk>[0-9]+)/$', views.rubrica_detail, name='rubrica_detail'),
	url(r'^nomi/new/$', views.rubrica_new, name='rubrica_new'),
	#url(r'^nomi/edit/$', views.rubrica_edit, name='rubrica_edit'),
	url(r'^nomi/(?P<pk>[0-9]+)/edit/$', views.rubrica_edit, name='rubrica_edit'),
	url(r'^nomi/(?P<pk>[0-9]+)/dettaglio/$', views.rubricaProfileView, name='rubrica_dettaglio'),
    #path('rubrica/<pk>/', views.rubricaProfileView, name="rubrica_dettaglio"),
	url(r'^nomi/newr/$', views.rubricar_new, name='rubricar_new'),
	url(r'^nomi/(?P<pk>[0-9]+)/dele/$', views.rubrica_delete, name='rubrica_delete'),
	url(r'^nomi/(?P<pk>[0-9]+)/deler/$', views.rubricar_delete, name='rubricar_delete'),
	url(r'^nomi/(?P<pk>[0-9]+)/editr/$', views.rubricar_edit, name='rubricar_edit'),

]