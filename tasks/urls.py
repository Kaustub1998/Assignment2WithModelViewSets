from django.urls import path, include
from rest_framework import routers,viewsets

from tasks.models import Comment, TaskAssignment
from tasks.serializers import CommentSerializer, TaskAssignmentSerializer
from.views import ProjectViewSet, TaskViewSet, TaskAssignmentViewSet, CommentViewSet, TaskCompletionView, OverdueTasksView, ProjectProgressView
from tasks import views

router = routers.DefaultRouter()
router.register(r'tasks', views.TaskViewSet, basename='tasks')
router.register(r'projects', views.ProjectViewSet, basename='projects')
router.register(r'task-assignments', views.TaskAssignmentViewSet, basename='task-assignments')
router.register(r'comments', views.CommentViewSet, basename='comments')

urlpatterns = [
    path('', include(router.urls)),
    path('tasks/<int:pk>/complete/', views.TaskCompletionView.as_view()),
    path('tasks/overdue', views.OverdueTasksView.as_view(), name='overdue-tasks'),
    path('projects/<int:pk>/progress/', views.ProjectProgressView.as_view()),
]
class TaskAssignmentViewSet(viewsets.ModelViewSet):
    queryset = TaskAssignment.objects.all()
    serializer_class = TaskAssignmentSerializer

class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer