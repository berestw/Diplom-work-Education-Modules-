from django.contrib import admin

from education_modules.models import EducationModules
from users.models import User

@admin.register(EducationModules)
class EduModelAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "name",
    )
