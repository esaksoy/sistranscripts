from django.contrib import admin
from . models import *
from import_export.admin import ImportExportModelAdmin

from django.contrib import admin


class StudentAdmin(ImportExportModelAdmin):
    list_display = ["studentid", "firstname","lastname","dateofbirth" ]
    search_fields = ["studentid"]
    list_per_page = 9
    pass


class ClassAdmin(admin.ModelAdmin):
    list_display = ["classid", "classname", "classyear"]
    pass


admin.site.register(Student, StudentAdmin)
admin.site.register(Class, ClassAdmin)





