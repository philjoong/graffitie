from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render

# Create your views here.
from django.urls import reverse

from accountapp.models import HelloWorld


def hello_world(request):

    if request.method == "POST":

        temp = request.POST.get("login_id")
        new_HelloWorld = HelloWorld()
        new_HelloWorld.text = temp
        new_HelloWorld.save()

        hello_world_list = HelloWorld.objects.all
        return HttpResponseRedirect(reverse('accountapp:hello_world'))
    else:
        hello_world_list = HelloWorld.objects.all
        return render(request, 'accountapp/content.html', context={'hello_world_list': hello_world_list})