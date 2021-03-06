from __future__ import absolute_import
from celery import shared_task
from django.core.mail import EmailMultiAlternatives
from django.template.loader import get_template
# from django.contrib.sites.shortcuts import get_current_site
from django.template import Context


@shared_task
def send_email(email_confirm):

    plaintext = get_template('registration/activation_email.txt')
    htmly = get_template('registration/email-template.html')
    # current_site = get_current_site(request)

    d = Context({
        'user': email_confirm.user,
        'activation_key': email_confirm.key
        # 'current_site': current_site
    })

    subject = 'Welcome to Doctorsinfo. Pakistan | Account activation'
    from_email = 'support@doctorsinfo.pk'
    to = email_confirm.email
    text_content = plaintext.render(d)
    html_content = htmly.render(d)
    msg = EmailMultiAlternatives(subject, text_content, from_email, [to])
    msg.attach_alternative(html_content, "text/html")
    msg.send()
