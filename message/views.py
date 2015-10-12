from django.shortcuts import render
from message.forms import MessageForm
from django.core.mail import send_mail
from django.conf import settings

def message(request):

	sent = False

	if request.method == 'POST':
		contact_form = MessageForm(data=request.POST)

		if contact_form.is_valid():
			message = contact_form.save()
			sent = True
            send_mail(request.POST['subject'], request.POST['message'], '', [settings.ADMIN_EMAIL], fail_silently=False)
		else:
			print contact_form.errors
	else:
		contact_form = MessageForm()
	
        return render(request, 'message.html', {'contact_form': contact_form, 'sent': sent})
