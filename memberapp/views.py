from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.http import HttpResponse, HttpResponseRedirect, HttpResponseForbidden
from django.shortcuts import render
from django.urls import reverse, reverse_lazy
from django.views.generic import CreateView, DetailView, UpdateView, DeleteView

from memberapp.forms import MemberUpdateForm
from memberapp.models import HelloWorld


# Create your views here.

def hello_world(request):

    if request.user.is_authenticated:
        if request.method == "POST":

            temp = request.POST.get('test_input')

            new_hello_world = HelloWorld()
            new_hello_world.text = temp
            new_hello_world.save()

            return HttpResponseRedirect(reverse('memberapp:hello_world'))
        else:
            hello_world_list = HelloWorld.objects.all()
            return render(request, 'memberapp/hello_world.html', context={'hello_world_list': hello_world_list })

    else:
        return HttpResponseRedirect(reverse('memberapp:login'))


class MemberCreateView(CreateView):
    model = User
    form_class = UserCreationForm
    success_url = reverse_lazy('memberapp:hello_world')
    template_name = 'memberapp/create.html'

class MemberDetailView(DetailView):
    model = User
    context_object_name = 'target_user'
    template_name = 'memberapp/detail.html'

class MemberUpdateView(UpdateView):
    model = User
    context_object_name = 'target_user'
    form_class = MemberUpdateForm
    success_url = reverse_lazy('memberapp:hello_world')
    template_name = 'memberapp/update.html'

    def get(self, *args, **kwargs):
        if self.request.user.is_authenticated and self.get_object() == self.request.user:
            return super().get(*args, **kwargs)
        else:
            return HttpResponseForbidden()

    def post(self, *args, **kwargs):
        if self.request.user.is_authenticated and self.get_object() == self.request.user:
            return super().post(*args, **kwargs)
        else:
            return HttpResponseForbidden()

class MemberDeleteView(DeleteView):
    model = User
    context_object_name = 'target_user'
    success_url = reverse_lazy('memberapp:login')
    template_name = 'memberapp/delete.html'

    def get(self, *args, **kwargs):
        if self.request.user.is_authenticated and self.get_object() == self.request.user:
            return super().get(*args, **kwargs)
        else:
            return HttpResponseForbidden()

    def post(self, *args, **kwargs):
        if self.request.user.is_authenticated and self.get_object() == self.request.user:
            return super().post(*args, **kwargs)
        else:
            return HttpResponseForbidden()