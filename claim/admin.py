from django.contrib import admin

from .models import Design, Functional, Claim, ClaimWithDoc


admin.site.register(Design)
admin.site.register(Functional)
admin.site.register(Claim)
admin.site.register(ClaimWithDoc)
