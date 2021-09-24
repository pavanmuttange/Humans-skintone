from . import views
from django.urls import path
from django.urls.conf import include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
   
    path('',views.index,name='index'),
    path('index.html',views.index,name='index'),
    path('skintone.html',views.skintone,name='skintone'),
    path('about.html',views.about,name='about'),
    path('SaveImage',views.SaveImage , name='SaveImage'),
    path('contact.html',views.contact , name='contact'),
    path('capture.html',views.capture , name='capture'),
    path('capturedimage',views.capturedimage , name='capturedimage'),
    path('help',views.help , name="help"),
]

urlpatterns = urlpatterns + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)