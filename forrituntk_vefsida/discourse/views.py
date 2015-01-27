from django.contrib.auth.decorators import login_required
from django.http import HttpResponseBadRequest, HttpResponseRedirect
from django.conf import settings

from discourse.discoursesso import DiscourseSSO

"""
Taken from https://meta.discourse.org/t/sso-example-for-django/14258
"""


@login_required
def sso(request):
    discourse_sso = DiscourseSSO(settings.DISCOURSE_SSO_SECRET)
    payload = request.GET.get('sso')
    signature = request.GET.get('sig')

    if None in [payload, signature]:
        return HttpResponseBadRequest('No SSO payload or signature. Please contact support if this problem persists.')

    # Validate the payload
    validated = discourse_sso.validate(payload=payload, sig=signature)

    if not validated:
        return HttpResponseBadRequest('Invalid payload. Please contact support if this problem persists.')

    # Build the return payload
    nounce = discourse_sso.get_nonce(payload)

    if nounce == '':
        return HttpResponseBadRequest("Nonce could not be found in payload")

    params = {
        'nonce': nounce,
        'email': request.user.email,
        'external_id': request.user.id,
        'username': request.user.username,
    }

    login_url = discourse_sso.build_login_url(params)

    # Redirect back to Discourse

    url = '%s/session/sso_login' % settings.DISCOURSE_BASE_URL
    return HttpResponseRedirect('%s?%s' % (url, login_url))