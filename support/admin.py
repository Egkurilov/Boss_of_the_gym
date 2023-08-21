from django.contrib import admin
from django.utils.html import format_html
from django.utils.safestring import mark_safe

# Register your models here.
from account.models import User
from support.models import Ticket


class SupportTicket(admin.ModelAdmin):
    list_display = (
        "id",
        "title",
        "user",
        "updated_on",
        "content",
        "created_on",
        "status",
    )

    list_filter = ("id", "user")


admin.site.register(Ticket, SupportTicket)
