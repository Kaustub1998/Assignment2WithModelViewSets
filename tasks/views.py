import datetime
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.views import APIView
from.models import Project, Task, TaskAssignment, Comment
from.serializers import ProjectSerializer, TaskSerializer, TaskAssignmentSerializer, CommentSerializer

class ProjectViewSet(viewsets.ModelViewSet):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer

class TaskViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer

class TaskAssignmentViewSet(viewsets.ModelViewSet):
    queryset = TaskAssignment.objects.all()
    serializer_class = TaskAssignmentSerializer

class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer

class TaskCompletionView(APIView):
    def post(self, request, pk):
        task = Task.objects.get(pk=pk)
        if task.status != 'in_progress':
            return Response({'error': 'Task is not in progress'}, status=400)
        task.status = 'completed'
        task.save()
        return Response({'message': 'Task completed successfully'})

class ProjectProgressView(APIView):
    def get(self, request, pk):
        project = Project.objects.get(pk=pk)
        tasks = project.tasks.all()
        completed_tasks = tasks.filter(status='completed')
        progress = (completed_tasks.count() / tasks.count()) * 100
        return Response({'progress': progress})

class OverdueTasksView(APIView):
    def get(self, request):
        tasks = Task.objects.filter(due_date__lt=datetime.date.today())
        serializer = TaskSerializer(tasks, many=True)
        return Response(serializer.data)
