from django.urls import path,include

from .views import ProjectAPIView,ProjectViewSet,TaskViewSet,CommentViewSet
from .views import TASKAPIREView

from rest_framework.routers import DefaultRouter

router=DefaultRouter()
router.register(r'projects',ProjectViewSet,basename='projects')
router.register(r'tasks',TaskViewSet,basename='tasks')
router.register(r'comments',CommentViewSet,basename='comments')


urlpatterns= [
]

urlpatterns += router.urls