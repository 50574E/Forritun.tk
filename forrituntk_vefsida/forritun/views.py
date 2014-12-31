from django.contrib.auth.forms import UserCreationForm
from django.http import HttpResponseRedirect
from django.shortcuts import render, render_to_response
from django.contrib import auth
from django.template import RequestContext


def index(request):
    if request.user.is_authenticated():
        return render(request, 'loggedIn.html')
    else:
        return render(request, 'index.html')


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
