from django.http import HttpResponse
from django.shortcuts import render
from django.template import loader
from django.core.mail import EmailMultiAlternatives
from django.shortcuts import get_object_or_404
from health.models import ResetPassword, User, UserProfile
from django.core.exceptions import ValidationError
from django.core.mail import EmailMultiAlternatives
from django.contrib.auth.hashers import make_password
from django.conf import settings
import datetime

from django import forms

class PasswordFrom(forms.Form):
    password1 = forms.CharField(label='Password', max_length=100)
    password2 = forms.CharField(label='Password', max_length=100)

def home_view(request):
    template = loader.get_template('error.html')
    return HttpResponse(template.render({}, request))

def reset_password_form(request, code):
    
    try:
        yesterday = datetime.datetime.now() - datetime.timedelta(1)
        code = get_object_or_404(ResetPassword, code=code, created__gt=yesterday)
        if code:
            profile = get_object_or_404(UserProfile, account_id=code.account_id)
            user = get_object_or_404(User, id=profile.user_id)
        else:
            context = {
                'Fail':'code not found',
            }
            template = loader.get_template('error.html')
            return HttpResponse(template.render(context, request))
        context = {
                'username': profile.name,
            }
    except Exception:
        context = {
            'Fail':'code not found',
            }
        template = loader.get_template('error.html')
        return HttpResponse(template.render(context, request))

    template = loader.get_template('main.html')
    if request.method == 'POST':
    # create a form instance and populate it with data from the request:
        if request.POST:
            post = request.POST
            if post.get('password1') == post.get('password2'):
                en_password = make_password(password=post.get('password1'), salt='cassaltmore', hasher='pbkdf2_sha1_cas')
                password = en_password.split('$')[3]
                user.set_password(password)
                user.save()
                code.delete()
                subject, from_email, to = 'CAS 비밀번호 변경 알림', settings.EMAIL_FROM, user.email
                text_content = ''
                d = { 'name': profile.name}
                email_template     = loader.get_template('email/success.html')
                html_content = email_template.render(d)
                msg = EmailMultiAlternatives(subject, text_content, from_email, [to])
                msg.attach_alternative(html_content, "text/html")
                send = msg.send()
                context = {
                    'success':True,
                    'msg' :'비밀번호 변경이 성공했습니다 !'
                }

            else:
                context = {
                    'fail': True,
                    'msg': "입력하신 비밀번호가 서로 맞지 않습니다. 다시 입력하세요."
                }
        
    return HttpResponse(template.render(context, request))
