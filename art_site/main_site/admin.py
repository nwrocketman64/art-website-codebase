from django.contrib import admin

# Import the needed models.
from .models import Request

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


# Register all the models that need to appear in admin.
admin.site.register(Request, RequestAdmin)