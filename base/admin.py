from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from base.forms import EmployerCreationForm
from base.models import Employer, Event


class EmployerAdmin(UserAdmin):
    add_form = EmployerCreationForm


    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username', 'password', 'password_confirm'),
        }),
    )

    def has_add_permission(self, request):
        if request.user.is_superuser:
            return True

    def has_change_permission(self, request, obj=None):
        if request.user.is_superuser:
            return True
        return False


class ScheduleAdmin(admin.ModelAdmin):
    pass

admin.site.register(Employer, EmployerAdmin)
admin.site.register(Event)
