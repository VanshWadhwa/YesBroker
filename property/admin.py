from django.contrib import admin
from .models import Property 


# Register your models here.

# admin.site.register(Property)
# # admin.site.register(Project)
from import_export.admin import ImportExportModelAdmin
# Register your models here.

# admin.site.register(Project)


@admin.register(Property)
class data(ImportExportModelAdmin):
    pass
