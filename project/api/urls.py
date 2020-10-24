from django.urls import path
from .views.default import welcome


urlpatterns = [ path('', welcome) ]
