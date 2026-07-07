from django.contrib import admin
from .models import DummyUser


@admin.register(DummyUser)
class DummyUserAdmin(admin.ModelAdmin):
    list_display = (
    "id",
    "name",
    "email",
    "pakistan_time",
    "utc_time",
    "converted_back_time",
)
    list_filter = ("pakistan_time",)
    search_fields = ("name", "email")