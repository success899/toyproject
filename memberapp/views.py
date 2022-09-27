from django.http import HttpResponse
from django.shortcuts import render

from memberapp.models import HelloWorld


# Create your views here.

def hello_world(request):

    if request.method == "POST":

        temp = request.POST.get('test_input')

        new_hello_world = HelloWorld()
        new_hello_world.text = temp
        new_hello_world.save()

        return render(request, 'memberapp/hello_world.html', context={'hello_world_output': new_hello_world })
    else:
        return render(request, 'memberapp/hello_world.html', context={'text': 'GET METHOD!'})