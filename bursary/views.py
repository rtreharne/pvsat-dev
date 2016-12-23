from django.shortcuts import render
from bursary.forms import BursaryForm 
from django.template.loader import render_to_string
from django.core.mail import send_mail, EmailMultiAlternatives
from django.conf import settings

def overview(request):
    return render(request, 'bursary.html', {})
    
def application(request):
    submitted = False

    if request.method == 'POST':
        bursary_form = BursaryForm(data=request.POST)
        
		
        if bursary_form.is_valid():
            bursary = bursary_form.save(commit=False)

            #Email confirmation to user
            subject = 'PVSAT Bursary Application | Submission Confirmation'

            text_content = render_to_string("burs_sub_conf.txt", {'bursary': bursary, 'URL': settings.SITE_URL})
            html_content = render_to_string("burs_sub_conf.html", {'bursary': bursary, 'URL': settings.SITE_URL})

            email = bursary.email

            msg1 = EmailMultiAlternatives(subject, text_content, '', [email])
            msg1.attach_alternative(html_content, "text/html")

            #Email confirmation to admin

            subject = 'Bursary application submitted by %s %s' % (bursary.first_name, bursary.last_name)

            text_content = render_to_string("burs_to_admin.txt", {'bursary': bursary, 'URL': settings.SITE_URL})

            msg2 = EmailMultiAlternatives(subject, text_content, '', [settings.ADMIN_EMAIL])

            if settings.EMAIL_STATUS:
                msg1.send()
                msg2.send()

            bursary_form.save()

            submitted = True

        else:
			print bursary_form.errors
    
    else:	    
	    bursary_form= BursaryForm()
	
    return render(request, 'bursary.html', {'bursary_form': bursary_form, 'submitted': submitted})

