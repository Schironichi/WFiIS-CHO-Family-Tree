from django_neomodel import admin as neo_admin
from .models import Person

class PersonAdmin(neo_admin.admin.ModelAdmin):
    list_display = (
        'uid',
        'name',
        'surname',
        'birth',
        'death'
        )
neo_admin.register(Person, PersonAdmin)