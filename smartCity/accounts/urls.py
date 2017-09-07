from django.conf.urls import url
from . import views
from django.contrib.auth import views as auth_views #as authviews to reference elsewhere

urlpatterns = [

    url(r'^$', views.account_page, name="main"),
    url(r'^login/$', auth_views.login, name="login"),
    url(r'^profile/$', views.login_success, name="success" ),
    url(r'^register/$', views.register, name="success" ),
    url(r'^logout/$', auth_views.logout, {'next_page': '/'}, name="logout"),

]