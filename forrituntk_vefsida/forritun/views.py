from django import forms
from django.contrib.admin import forms as admin_forms
from django.contrib.auth import views
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect
from django.shortcuts import render, render_to_response
from django.contrib import auth
from django.template import RequestContext
from django.views.generic import ListView
from taggit.models import Tag
from forritun.models import ProgrammingLanguage, Resource


def index(request):
    languages = ProgrammingLanguage.objects.order_by('-date_created')[:5]
    context = {'languages': languages, 'active_navigation': "home"}
    if request.user.is_authenticated():
        return render(request, 'loggedIn.html', context)
    else:
        return render(request, 'index.html', context)


def login_view(request):
    return views.login(request, template_name='registration/login.html', authentication_form=admin_forms.AuthenticationForm)


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

    def get_context_data(self, **kwargs):
        context = super(ProgrammingLanguageListView, self).get_context_data(**kwargs)
        context['active_navigation'] = "language-list"
        return context


class ResourceListView(ListView):
    model = Resource
    template_name = 'resourceList.html'

    def get_context_data(self, **kwargs):
        context = super(ResourceListView, self).get_context_data(**kwargs)
        context['active_navigation'] = "language-list"
        try:
            context['name'] = ProgrammingLanguage.objects.get(id=self.kwargs['id'])
            context['tags'] = Tag.objects.filter(resource__language__id=self.kwargs['id']).distinct()
        except ProgrammingLanguage.DoesNotExist:
            context['name'] = "Forritunarmál"
        return context

    def get_queryset(self):
        return Resource.objects.filter(language__id=self.kwargs['id'])