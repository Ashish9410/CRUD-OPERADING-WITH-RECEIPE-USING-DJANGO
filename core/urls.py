from django.contrib import admin
from django.urls import path
from vege.views import vege, dltrec, update_recepi
from home.views import home, contact, about, success_page

from django.conf import settings
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    path('', home, name='home'),
    path('veges/', vege, name='vege'),
    path('dltrec/<id>/', dltrec, name='dltrec'),
    path('update_recepi/<id>/', update_recepi, name='update_recepi'),
    path('contact/', contact, name='contact'),
    path('about/', about, name='about'),
    path('success-page/', success_page, name='success-page'),
    path('admin/', admin.site.urls),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

urlpatterns += staticfiles_urlpatterns()
