from django.shortcuts import render
from django.views import generic
from django.views.decorators.cache import cache_page
from django.utils.decorators import method_decorator

from rest_framework import viewsets

from .models import Project
from .serializers import ProjectSerializer


class ProjectList(generic.ListView):
    model = Project
    template_name = 'projects/project_list.html'


class ProjectDetail(generic.DetailView):
    model = Project
    template_name = 'projects/project_detail.html'


class ProjectViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows projects to be viewed or edited.
    """
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer

    @method_decorator(cache_page(60*60))
    def dispatch(self, *args, **kwargs):
        return super(ProjectViewSet, self).dispatch(*args, **kwargs)