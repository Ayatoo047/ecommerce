from django.contrib import admin
from .models import *


class OtpAdmin(admin.ModelAdmin):
    readonly_fields = ['created', 'profile']
    fields = ['profile','otp', 'created']
# Register your models here.
admin.site.register(Profile)
admin.site.register(Shop)
admin.site.register(Otp, OtpAdmin)

