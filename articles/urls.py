from django.urls import path
from django.conf.urls import include,url
from . import views

app_name = 'articles'

urlpatterns = [
  
  #path('',views.articles_list),
  #path('',views.article_detail),
  url(r'^$',views.articles_list,name="list"),

  #url to create a new article
  url(r'^create/$',views.article_create,name="create"),

  #a named capturing group
  #To create a named capturing group we have to say ?P
  #In angular brackets we have to write the name of the thing we want to capture
  #\w:any type of letter,underscore
  #^:start
  # $:end
  # - means: - can also be included in url
  # + means: that thing before it can be of any length
  url(r'^(?P<slug>[\w-]+)/$',views.articles_details,name="detail"),

]
