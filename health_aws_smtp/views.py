from django.http import HttpResponse
from django.shortcuts import render
import datetime

def current_datetime(request, pk):

    now = datetime.datetime.now()
    # html = "<html><body>It is now %s. %s</body></html>" %now  %now
    return render(request, 'health_aws_smtp/templates/main.html', {})