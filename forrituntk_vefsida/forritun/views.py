from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
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


def logout_view(request):
    auth.logout(request)

    return HttpResponseRedirect("/")


def register(request):
    if request.method == 'POST':
        form = EmailUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect("/accounts/login")
    else:
        form = EmailUserCreationForm()
    c = {'form': form}
    return render_to_response("registration/register.html", c, context_instance=RequestContext(request))


class EmailUserCreationForm(UserCreationForm):
    email = forms.EmailField(max_length=75)

    class Meta:
        model = User
        fields = ("email",)

    def save(self, commit=True):
        user = super(EmailUserCreationForm, self).save(commit=False)
        user.email = self.cleaned_data["email"]
        if commit:
            user.save()
        return user


class ProgrammingLanguageListView(ListView):
    model = ProgrammingLanguage
    template_name = 'languages.html'


class ResourceListView(ListView):
    model = Resource
    template_name = 'resourceList.html'

    def get_queryset(self):
        return Resource.objects.filter(language__id=self.kwargs['id'])