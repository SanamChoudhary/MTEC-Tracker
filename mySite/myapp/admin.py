from django.contrib import admin
from .models import studentInformationModel,dateOfCleanup

# Register your models here.

admin.site.register(dateOfCleanup)
admin.site.register(studentInformationModel)
