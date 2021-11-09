from django.contrib import admin
from .models import ServiceModel
from .models import Schedule, TypeService

admin.site.register(Schedule)
admin.site.register(TypeService)
admin.site.register(ServiceModel)
# Register your models here.
