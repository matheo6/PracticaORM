from django.urls import path

from .views import ProjectAPIView
from .views import TASKAPIREView

urlpatterns= [
    path('projects/', ProjectAPIView.as_view()),
    path('task/', TASKAPIREView.as_view())
]