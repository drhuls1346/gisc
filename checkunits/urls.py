from django.conf.urls import patterns, include, url
from .views import WelcomeView
from .views import AboutUsView

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'gisc.views.home', name='home'),
    # url(r'^gisc/', include('gisc.foo.urls')),
    url(r'^welcome$', WelcomeView.as_view(), name='welcome'),
    url(r'^aboutus$', AboutUsView.as_view(), name='aboutus'),
)
