from django.contrib import admin
from django.contrib.auth import get_user_model

from core.models import State, Incident
from core.forms import UserAdminFormCustomizer


@admin.register(get_user_model())
class CustomUserAdmin(admin.ModelAdmin):
    form = UserAdminFormCustomizer
    list_display = ['__str__', 'email', 'is_active',]
    fieldsets = (
        ("User information", {
            'fields': [
                'username', 'email', 'first_name', 'last_name', 'avatar',
            ]
        }),
        ("User validity", {'fields': ['admin', 'active', 'staff',]}),

        ###
        ### the below will remain commented out until permission has been 
        ### configured to accept blank (not_required)
        ###

        # # Making user permissions and groups collapsible
        # ("User permissions", {
        #     'fields': [ 'permissions', 'groups'],
        #     'classes': ('collapse',),
        #     }
        # )
    )


@admin.register(Incident)
class Incident (admin.ModelAdmin):
    list_display = ['__str__', 'date_uploaded']



@admin.register(State)
class StateAdmin(admin.ModelAdmin):
    list_display = ['__str__', ]


