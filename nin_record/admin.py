from django.contrib import admin
from .models import NINProfile, SupportingDocument, Parent, Guardian, NextOfKin, RegistrationCenter

# Register your models here.

admin.site.register(NINProfile)
admin.site.register(SupportingDocument)
admin.site.register(Parent)
admin.site.register(Guardian)
admin.site.register(NextOfKin)
admin.site.register(RegistrationCenter)