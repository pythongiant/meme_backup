from django.conf.urls import url
from . import views
from .models import Memes
urlpatterns=[
    url(r'^$',views.index,name="index"),
    url(r'^memes',views.memesPage,name="memes_home"),
    url(r'^0',views.PageRedirect,name="redirect"),
    url(r'^'+str(Memes.objects.count()+2),views.PageMoreRedirect,name="more_redirect"),
    url(r'^14',views.Mistake_redirect),
    url(r'^(?P<meme_id>[0-9]+)/$',views.detail,name="meme_detail")
] 
