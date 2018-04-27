from django.http import HttpResponse
from django.shortcuts import render
from django.template import loader

import datetime

from django import forms

class PasswordFrom(forms.Form):
    password = forms.CharField(label='Password', max_length=100)

def reset_password_form(request, account_id):


    if request.method == 'POST':
    # create a form instance and populate it with data from the request:
        form = PasswordFrom(request.POST)
    # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            template = loader.get_template('main.html')
            context = {
                'latest_question_list': 'google',
            }
            return HttpResponse(template.render(context, request))
    # now = datetime.datetime.now()
    # html = "<html><body>It is now %s. %s</body></html>" %now  %now
    template = loader.get_template('main.html')
    context = {
        'latest_question_list': '',
        'link_expire': True
    }
    return HttpResponse(template.render(context, request))
    # return render(request, 'health_aws_smtp/templates/', {})