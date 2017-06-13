from django.contrib import admin
from .models import Pibpatient, Pibrecord, User
from .models import Fetpersons, Fetrecords, Fetusers, Fetrecordimages

# Register your models here.

admin.site.register(Pibpatient)
admin.site.register(Pibrecord)
admin.site.register(User)
admin.site.register(Fetpersons)
admin.site.register(Fetrecords)
admin.site.register(Fetusers)
admin.site.register(Fetrecordimages)
