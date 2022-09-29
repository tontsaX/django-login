from django.urls import path
from .views import TiliView

urlpatterns = [
    path('', TiliView.as_view(), name='tili'),
]