from django.contrib import admin
from core.models import Company, Country, Millionaire, VoteMillionaire


class MillionaireAdmin(admin.ModelAdmin):
    list_display = ('name','country','city', 'profession')
    search_fields = ['name',]


admin.site.register(Company)
admin.site.register(Country)
admin.site.register(Millionaire, MillionaireAdmin)
admin.site.register(VoteMillionaire)
