from django.contrib import admin


# Register your models here.
class MyModelAdmin(admin.ModelAdmin):
    fieldsets = (
        (
            "My Model",
            {
                "fields": ("string_field", "integer_field", "boolean_field", "date_field"),
            },
        ),
    )
    list_display = ["string_field", "integer_field", "boolean_field", "date_field"]
    search_fields = ["string_field", "integer_field", "boolean_field", "date_field"]
