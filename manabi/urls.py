from django.conf.urls.defaults import *
from django.views.generic.simple import direct_to_template
from forms import SignupForm
from utils.urldecorators import decorated_patterns
from lazysignup.decorators import allow_lazy_user
from utils.authforms import PinaxLazyConvertForm
import settings

from django.contrib import admin
admin.autodiscover()

from flashcards.urls import rest_api_urlpatterns


urlpatterns = patterns('',
    # Use our customized form
    url(r'^account/signup/$', 'account.views.signup',
        name="acct_signup", kwargs={'form_class': SignupForm}), 

    url(r'^convert/convert/$', 'lazysignup.views.convert',
        name='lazysignup_convert',
        kwargs={
            'form_class': PinaxLazyConvertForm,
            'email_verification': settings.ACCOUNT_EMAIL_VERIFICATION,
            'verification_sent_template_name': 'account/verification_sent.html',
            'success_url': '',
        }),

    (r'^account/', include('account.urls')),
    (r'^admin/', include(admin.site.urls)),
    #(r'^sentry/', include('sentry.web.urls')),

    (r'^mobile-account/', include('mobileaccount.urls')),

    url(r'^popups/login/$', 'account.views.login', name='popup_acct_login', kwargs={
        'template_name': 'popups/login.html',}),

    (r'^popups/', include('popups.urls')),

    url(r'^terms-of-service/$', direct_to_template,
        {'template': 'tos.html'}, name='terms_of_service'),
    url(r'^privacy-policy/$', direct_to_template,
        {'template': 'privacy.html'}, name='privacy_policy'),
    url(r'^credits/$', direct_to_template,
        {'template': 'credits.html'}, name='credits'),

    url(r'^flashcards/api/', include(rest_api_urlpatterns)),

) + decorated_patterns('', allow_lazy_user,
    #url(r'^$', direct_to_template, {
    #    "template": "homepage.html",
    #}, name="home"),
    url(r'^$', 'views.index', name='home'),

    url(r'^home/$', 'views.home', name='home_inline'),
    
    #url(r'^admin/invite_user/$', 'signup_codes.views.admin_invite_user',
        #name="admin_invite_user"),


    #(r'^profiles/', include('basic_profiles.urls')),
    #url(r'^profiles/', include('idios.urls')),

    (r'^about/', include('about.urls')),
    
    # my own
    #(r'^reports/', include('reports.urls')),
    (r'^dojango/', include('dojango.urls')),
    (r'^flashcards/', include('flashcards.urls')),
    (r'^textbooks/', include('books.urls')),
    (r'^importer/', include('importer.urls')),
    (r'^jdic/', include('jdic.urls')),
    (r'^kanjivg/', include('kanjivg.urls')),
    (r'^stats/', include('stats.urls')),
)

if settings.SERVE_MEDIA:
    urlpatterns += patterns('',
        (r'^favicon\.ico$', 'django.views.generic.simple.redirect_to', {'url': '/site_media/static/favicon.ico'}),
    )

    from django.contrib.staticfiles.urls import staticfiles_urlpatterns
    urlpatterns += staticfiles_urlpatterns()

    #urlpatterns += patterns('', 
    #    #(r'^site_media/', include('staticfiles.urls')),
    #    url(r'', include('staticfiles.urls')),
    #)
