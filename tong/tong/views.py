from django.shortcuts import redirect
from django.core.urlresolvers import reverse


def get_home(request):
    return redirect(reverse('about:resume'))
