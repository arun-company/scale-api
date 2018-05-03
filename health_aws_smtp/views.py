from django.http import HttpResponse
from django.shortcuts import render
from django.template import loader
from django.core.mail import EmailMultiAlternatives
from django.shortcuts import get_object_or_404
from health.models import ResetPassword, User, UserProfile
from django.core.exceptions import ValidationError
import datetime

from django import forms

class PasswordFrom(forms.Form):
    password1 = forms.CharField(label='Password', max_length=100)
    password2 = forms.CharField(label='Password', max_length=100)

def reset_password_form(request, code):
    
    try:
        code = get_object_or_404(ResetPassword, code=code)
        profile = get_object_or_404(UserProfile, account_id=code.account_id)
        user = get_object_or_404(User, id=profile.user_id)
        
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
                user.set_password(post.get('password1'))
                user.save()
                ResetPassword.objects.filter(account_id = profile.account_id).delete()
                #TODO: Will Send Success Message.
                # subject, from_email, to = 'CAS 비밀번호 변경 요청', 'no-reply@mail.mylitmus.cloud', email
                # text_content = ''
                # site_url = settings.BASE_URL
                # d = { 'name': profile.name}
                # email_template     = loader.get_template('email/reset-password-inline.html')
                # html_content = email_template.render(d)
                # msg = EmailMultiAlternatives(subject, text_content, from_email, [to])
                # msg.attach_alternative(html_content, "text/html")
                # send = msg.send()
                context = {
                    'success':True,
                    'msg' :'비밀번호 변경이 성공했습니다 !'
                }

            else:
                context = {
                    'fail': True,
                    'msg': "Password Confirmation doesn't match"
                }
        
    return HttpResponse(template.render(context, request))
