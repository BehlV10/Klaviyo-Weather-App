from django.http import HttpResponse
import json
from urllib.request import urlopen
from django.template import loader
from django.shortcuts import get_object_or_404, render
from django.http import *
from django.core.exceptions import ValidationError
from django.db import IntegrityError

from .models import WeatherSubscription

def index(request):
    return render(request, 'signup/index.html', {'location_set': WeatherSubscription.city_choices})

def confirm(request):
    ws = WeatherSubscription(email=request.POST['email_input'], location=request.POST['location_input'])
    render_kwargs = {}
    try:
        ws.clean_fields()
        ws.save()
    except ValidationError as e:
        render_kwargs['invalid_message'] = 'Email not in a standard form.'
    except IntegrityError as e:
        render_kwargs['invalid_message'] = 'Email already subscribed.'
    return render(request, 'signup/confirm.html', render_kwargs)