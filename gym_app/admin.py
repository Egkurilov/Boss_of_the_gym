from django.contrib import admin
from django.utils.html import format_html
from django.utils.safestring import mark_safe

# Register your models here.
from account.models import User
from exercises.models import ExerciseList


class UserList(admin.ModelAdmin):
    list_display = (
        "id",
        "first_name",
        "last_name",
        "email",
        "last_login",
    )
    readonly_fields = ("avatar_image",)

    list_filter = ("id", "username")

    @admin.display(description="Аватар пользователя")
    def avatar_image(self, obj):
        return mark_safe(
            f'<img src="data:image/png;base64, {obj.avatar}" class="imaged w64 rounded">'
        )


class  Exercises(admin.ModelAdmin):
    list_display = ("id", "name", "cost", "type")
    list_filter = ("type",)


admin.site.register(User, UserList)
admin.site.register(ExerciseList, Exercises)
