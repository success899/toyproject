from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.urls import reverse, reverse_lazy
from django.utils.decorators import method_decorator
from django.views.generic import ListView, CreateView, DetailView, DeleteView
from django.views.generic.list import MultipleObjectMixin

from articleapp.models import Article
from projectapp.forms import ProjectCreationForm
from projectapp.models import Project
from subscribeapp.models import Subscription


# Create your views here.

@method_decorator(login_required(login_url='/members/login'), 'get')
@method_decorator(login_required(login_url='/members/login'), 'post')
class ProjectCreateView(CreateView):
    model = Project
    form_class = ProjectCreationForm
    template_name = 'projectapp/create.html'

    def get_success_url(self):
        return reverse('projectapp:detail', kwargs={'pk': self.object.pk})

class ProjectDetailView(DetailView, MultipleObjectMixin):
    model = Project
    context_object_name = 'target_project'
    template_name = 'projectapp/detail.html'

    paginate_by = 30

    def get_context_data(self, **kwargs):

        project = self.object
        user = self.request.user

        if user.is_authenticated:
            subscription = Subscription.objects.filter(user=user, project=project)
        else:
            subscription = None

        object_list = Article.objects.filter(project=self.get_object())
        return super(ProjectDetailView, self).get_context_data(object_list=object_list, subscription=subscription, **kwargs)

class ProjectListView(ListView):
    model = Project
    context_object_name = 'project_list'
    template_name = 'projectapp/list.html'
    paginate_by = 30

# 추후 특정 인원만 지울 수 있게 권한 설정 필요
@method_decorator(login_required(login_url='/articles/list'), 'get')
@method_decorator(login_required(login_url='/articles/list'), 'post')
class ProjectDeleteView(DeleteView):
    model = Project
    context_object_name = 'target_project'
    template_name = 'projectapp/delete.html'
    success_url = reverse_lazy('projectapp:list')
