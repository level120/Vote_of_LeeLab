"""
Definition of urls for Vote_of_LeeLab.
"""

from datetime import datetime
from django.conf.urls import url, handler400, handler403, handler404, handler500
from django.contrib.staticfiles.views import serve
import django.contrib.auth.views

import app.forms
import app.views
import VoteApp.views

# Uncomment the next lines to enable the admin:
from django.conf.urls import include
from django.contrib import admin
admin.autodiscover()

handler400 = 'VoteApp.views.handler400'
handler403 = 'VoteApp.views.handler403'
handler404 = 'VoteApp.views.handler404'
handler500 = 'VoteApp.views.handler500'

urlpatterns = [
    # Examples:
    url(r'^$', VoteApp.views.index, name='index'),
    url(r'^about$', VoteApp.views.about, name='about'),
    url(r'^vote$', VoteApp.views.vote, name='vote'),
    url(r'^capstone_design$', VoteApp.views.capstone, name='capstone'),
    url(r'^signup$', VoteApp.views.signup, name='signup'),
    url(r'^login/$',
        django.contrib.auth.views.login,
        {
            'template_name': 'VoteApp/login.html',
            'authentication_form': VoteApp.forms.BootstrapAuthenticationForm,
            'extra_context':
            {
                'title': 'Log in',
                'year': datetime.now().year,
            }
        },
        name='login'),
    url(r'^logout$',
        django.contrib.auth.views.logout,
        {
            'next_page': '/',
        },
        name='logout'),

    # if DEBUG set False, it needs.
    url(r'^static/(?P<path>.*)$', serve, kwargs={'insecure': True}),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
     url(r'^admin/', admin.site.urls),

     # Social Login
     url('', include('social_django.urls', namespace='social')),

     # Like & Dislike
     url(r'^like/$', VoteApp.views.like, name='like'),
     url(r'^like_anonymous/$', VoteApp.views.like_anonymous, name='like_anonymous'),
     url(r'^like_ready/$', VoteApp.views.like_ready, name='like_ready'),
]
