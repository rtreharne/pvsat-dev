from django.contrib import admin
from bursary.models import Applicant


class ApplicantAdmin(admin.ModelAdmin):
    list_display = ('last_name', 'first_name', 'view_email', 'institution', 'supervisor', 'status')

    def view_email(self, obj):
        return u"<a href='mailto:%s'>%s</a>" % (obj.email, obj.email)
    view_email.allow_tags = True
    view_email.short_description = 'email'

admin.site.register(Applicant, ApplicantAdmin)


