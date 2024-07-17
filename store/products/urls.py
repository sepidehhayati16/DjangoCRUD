
from django.urls import path
from . import views
urlpatterns = [
    path('crad/', views.crad, name='store'),
]