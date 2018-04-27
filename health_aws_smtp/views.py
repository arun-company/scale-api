from django.http import HttpResponse
from django.shortcuts import render
from django.template import loader

import datetime

def current_datetime(request, pk):

    now = datetime.datetime.now()
    # html = "<html><body>It is now %s. %s</body></html>" %now  %now
    template = loader.get_template('main.html')
    context = {
        'latest_question_list': '',
    }
    return HttpResponse(template.render(context, request))
    # return render(request, 'health_aws_smtp/templates/', {})