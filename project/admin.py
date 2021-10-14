from django.contrib import admin
from .models import Project
# from import_export.admin import ImportExportModelAdmin
from import_export.admin import ImportExportModelAdmin
# Register your models here.

# admin.site.register(Project)


@admin.register(Project)
class data(ImportExportModelAdmin):
    pass
