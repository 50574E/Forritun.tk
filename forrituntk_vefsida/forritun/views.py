from django.contrib.auth.forms import UserCreationForm
from django.http import HttpResponseRedirect
from django.shortcuts import render, render_to_response
from django.contrib import auth
from django.template import RequestContext
from django.views.generic import ListView
from forritun.models import ProgrammingLanguage, Resource


def index(request):
    languages = ProgrammingLanguage.objects.order_by('-date_created')[:5]
    context = {'languages': languages}
    if request.user.is_authenticated():
        return render(request, 'loggedIn.html', context)
    else:
        return render(request, 'index.html', context)


def login_view(request):
    username = request.POST.get('username', '')
    password = request.POST.get('password', '')
    user = auth.authenticate(username=username, password=password)
    if user is not None and user.is_active:
        # Tókst að skrá inn
        auth.login(request, user)
        return HttpResponseRedirect("/")
    else:
        # Tekst ekki að skrá inn
        return HttpResponseRedirect("/")


def logout_view(request):
    auth.logout(request)

    return HttpResponseRedirect("/")


def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            new_user = form.save()
            return HttpResponseRedirect("/accounts/login")
    else:
        form = UserCreationForm()
    c = {'form': form}
    return render_to_response("registration/register.html", c, context_instance=RequestContext(request))


class ProgrammingLanguageListView(ListView):
    model = ProgrammingLanguage
    template_name = 'languages.html'


class ResourceListView(ListView):
    model = Resource
    template_name = 'resourceList.html'

    def get_queryset(self):
        return Resource.objects.filter(language__id=self.kwargs['id'])