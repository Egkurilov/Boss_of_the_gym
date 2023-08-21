from django.contrib import admin
from django.utils.html import format_html
from django.utils.safestring import mark_safe

# Register your models here.
from account.models import User
from support.models import Ticket
from support.models import TicketMessage


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


class SupportTicketMessage(admin.ModelAdmin):
    list_display = (
        "id",
        "ticket_id",
        "to_user",
        "updated_on",
        "content",
    )

    list_filter = ("ticket_id", "to_user")


admin.site.register(Ticket, SupportTicket)
admin.site.register(TicketMessage, SupportTicketMessage)
