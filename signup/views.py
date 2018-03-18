<<<<<<< HEAD
"""
WSGI config for Weather_App project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/2.0/howto/deployment/wsgi/
"""

from django.http import HttpResponse
import json
from urllib.request import urlopen
from django.template import loader
from django.shortcuts import get_object_or_404, render
from django.http import *
from django.core.exceptions import ValidationError
from django.db import IntegrityError

from .models import WeatherSubscription

# Create your views here.

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

def weather(request, question_id):
    return HttpResponse("You're looking at question %s." % question_id)

    """
    html = urlopen("http://www.google.com/")
    # print(html)
    key = "6e677fb094c89662"
    # zip_code = input('For which ZIP code would you like to see the weather? ')
    city = "Cedar_Rapids"
    zipcode = 10040
    # fileName = "http://api.wunderground.com/api/" + key +    "/geolookup/conditions/q/PA/" + zip_code + ".json"
    f = urlopen('http://api.wunderground.com/api/' + key + '/geolookup/conditions/q/IA/' + city + '.json')
    json_string = f.read()
    parsed_json = json.loads(json_string)
    location = parsed_json['location']['city']
    temp_f = parsed_json['current_observation']['temp_f']
    #print "Current temperature in %s is: %s" % (location, temp_f)
    print ("Current temperature in %s is: %s" % (location, temp_f))
    f.close()
    url = 'http://samples.openweathermap.org/data/2.5/weather?zip={0},us&appid=0b7f3cd153bc12d3accb83f9682bccbb'.format(zipcode) # if zipcode is defined
    response = urlopen(url)
    response.read()
    """
=======
"""
WSGI config for Weather_App project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/2.0/howto/deployment/wsgi/
"""

from django.http import HttpResponse
import json
from urllib.request import urlopen
from django.template import loader
from django.shortcuts import get_object_or_404, render
from django.http import *
from django.core.exceptions import ValidationError
from django.db import IntegrityError

from .models import WeatherSubscription

# Create your views here.

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

def weather(request, question_id):
    return HttpResponse("You're looking at question %s." % question_id)

    """
    html = urlopen("http://www.google.com/")
    # print(html)
    key = "6e677fb094c89662"
    # zip_code = input('For which ZIP code would you like to see the weather? ')
    city = "Cedar_Rapids"
    zipcode = 10040
    # fileName = "http://api.wunderground.com/api/" + key +    "/geolookup/conditions/q/PA/" + zip_code + ".json"
    f = urlopen('http://api.wunderground.com/api/' + key + '/geolookup/conditions/q/IA/' + city + '.json')
    json_string = f.read()
    parsed_json = json.loads(json_string)
    location = parsed_json['location']['city']
    temp_f = parsed_json['current_observation']['temp_f']
    #print "Current temperature in %s is: %s" % (location, temp_f)
    print ("Current temperature in %s is: %s" % (location, temp_f))
    f.close()
    url = 'http://samples.openweathermap.org/data/2.5/weather?zip={0},us&appid=0b7f3cd153bc12d3accb83f9682bccbb'.format(zipcode) # if zipcode is defined
    response = urlopen(url)
    response.read()
    """
>>>>>>> b9f72242a35fadfe8364a8f9e0c3decc1de12986
    return HttpResponse("Hello, world. You're at the Weather index.")