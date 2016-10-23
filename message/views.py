from django.shortcuts import render
from django.template.loader import render_to_string
from message.forms import MessageForm
from django.core.mail import send_mail, EmailMultiAlternatives
from django.conf import settings

def message(request):

    sent = False

    if request.method == 'POST':
        contact_form = MessageForm(data=request.POST)

        if contact_form.is_valid():
            message = contact_form.save()

            subject = 'PVSAT Enquiry from %s %s' % (message.first_name, message.last_name)

            text_content = render_to_string("message_temp.txt", {'message' : message})

            msg = EmailMultiAlternatives(subject, text_content, '', [settings.DEFAULT_FROM_EMAIL])

            if settings.EMAIL_STATUS:
                msg.send()

            #send_mail(request.POST['subject'], request.POST['message'], '', [settings.ADMIN_EMAIL], fail_silently=False)
            sent = True
        else:
            print contact_form.errors
    else:
        contact_form = MessageForm()

    return render(request, 'message.html', {'contact_form': contact_form, 'sent': sent})
