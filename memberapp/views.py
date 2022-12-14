from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.http import HttpResponse, HttpResponseRedirect, HttpResponseForbidden
from django.shortcuts import render
from django.urls import reverse, reverse_lazy
from django.utils.decorators import method_decorator
from django.views.generic import CreateView, DetailView, UpdateView, DeleteView
from django.views.generic.list import MultipleObjectMixin

from articleapp.models import Article
from memberapp.decorators import member_owner_verification
from memberapp.forms import MemberUpdateForm

verification = [ login_required(login_url='/members/login'), member_owner_verification ]

# Create your views here.

class MemberCreateView(CreateView):
    model = User
    form_class = UserCreationForm
    success_url = reverse_lazy('articleapp:list')
    template_name = 'memberapp/create.html'

class MemberDetailView(DetailView, MultipleObjectMixin):
    model = User
    context_object_name = 'target_user'
    template_name = 'memberapp/detail.html'

    paginate_by = 30

    def get_context_data(self, **kwargs):
        object_list = Article.objects.filter(writer=self.get_object())
        return super(MemberDetailView, self).get_context_data(object_list=object_list, **kwargs)

@method_decorator(verification, 'get')
@method_decorator(verification, 'post')
class MemberUpdateView(UpdateView):
    model = User
    context_object_name = 'target_user'
    form_class = MemberUpdateForm
    success_url = reverse_lazy('articleapp:list')
    template_name = 'memberapp/update.html'


@method_decorator(verification, 'get')
@method_decorator(verification, 'post')
class MemberDeleteView(DeleteView):
    model = User
    context_object_name = 'target_user'
    success_url = reverse_lazy('memberapp:login')
    template_name = 'memberapp/delete.html'
