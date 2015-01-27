from django.contrib.auth.decorators import login_required
from django.conf import settings
from django.shortcuts import redirect

from discourse.sso import sso_validate, sso_redirect_url

"""
Taken from https://meta.discourse.org/t/sso-example-for-django/14258
"""

SECRET = settings.DISCOURSE_SSO_SECRET

@login_required
def sso(request):
    payload = request.GET.get('sso')
    signature = request.GET.get('sig')
    nonce = sso_validate(payload, signature, SECRET)
    url = sso_redirect_url(nonce, SECRET, request.user.email, request.user.id, request.user.username)
    return redirect('http://discourse.forritun.tk' + url)
