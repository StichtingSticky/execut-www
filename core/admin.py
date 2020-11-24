from django.contrib import admin
from .models import *

# Register your models here.

admin.site.register(Site)
admin.site.register(Committee)
admin.site.register(CommissionerRole)
admin.site.register(Commissioner)
admin.site.register(Speaker)
admin.site.register(Activity)
admin.site.register(Sponsor)
admin.site.register(SponsorshipTier)