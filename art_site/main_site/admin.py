from django.contrib import admin

# Import the needed models.
from .models import Request, Work

# Register your models here.


class RequestAdmin(admin.ModelAdmin):
    """Request Admin
    The class controls how Requests will appear in the admin.
    """
    readonly_fields = (
        "first_name",
        "last_name",
        "email",
        "comment",
        "sent_time",
    )


class WorkAdmin(admin.ModelAdmin):
    """ Work Admin
    The class controls how the works appear in the admin sections.
    """
    readonly_fields = (
        "date",
    )


# Register all the models that need to appear in admin.
admin.site.register(Request, RequestAdmin)
admin.site.register(Work, WorkAdmin)