from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse, reverse_lazy
from django.views.generic import CreateView

from memberapp.models import HelloWorld


# Create your views here.

def hello_world(request):

    if request.method == "POST":

        temp = request.POST.get('test_input')

        new_hello_world = HelloWorld()
        new_hello_world.text = temp
        new_hello_world.save()

        return HttpResponseRedirect(reverse('memberapp:hello_world'))
    else:
        hello_world_list = HelloWorld.objects.all()
        return render(request, 'memberapp/hello_world.html', context={'hello_world_list': hello_world_list })



class MemberCreateView(CreateView):
    model = User
    form_class = UserCreationForm
    success_url = reverse_lazy('memberapp:hello_world')
    template_name = 'memberapp/create.html'