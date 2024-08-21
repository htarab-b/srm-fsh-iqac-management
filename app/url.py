from django.urls import path
from .views import *

urlpatterns = [
    path('login', LoginView.as_view(), name='login'),
    path('', FormFillView.as_view(), name='form'),
    path('admin', AdminView.as_view(), name='admin')
]