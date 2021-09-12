from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render

# Create your views here.
from django.urls import reverse, reverse_lazy
from django.views.generic import CreateView, DetailView, UpdateView, DeleteView

from accountapp.forms import AccountUpdateForm
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


class AccountCreateView(CreateView):
    model = User
    form_class = UserCreationForm
    success_url = reverse_lazy('accountapp:hello_world')
    template_name = 'accountapp/create.html'


# class LoginView():

# class LogoutView():

class AccountDetailView(DetailView):
    model = User
    context_object_name = 'target_user'
    template_name = 'accountapp/detail.html'

class AccountUpdateView(UpdateView):
    model = User
    form_class = AccountUpdateForm
    success_url = reverse_lazy('accountapp:hello_world')
    template_name = 'accountapp/update.html'

class AccountDeleteView(DeleteView):
    model = User
    success_url = reverse_lazy('accountapp:login')
    template_name = 'accountapp/delete.html'