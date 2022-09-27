from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

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