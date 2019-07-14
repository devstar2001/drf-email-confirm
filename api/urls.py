from django.conf.urls import include, url
from django.urls import path
from django.contrib import admin
from django.views.generic import TemplateView, RedirectView

from rest_framework_swagger.views import get_swagger_view
schema_view = get_swagger_view(title='Pastebin API')
from . import views

urlpatterns = [


    path('swagger/', schema_view)
]
