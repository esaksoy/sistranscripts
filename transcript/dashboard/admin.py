from django.contrib import admin
from . models import *
from import_export.admin import ImportExportModelAdmin



class DataAdmin(ImportExportModelAdmin):
    list_display = ["studentid", "fistname","surname","dateofbirth" ]
    search_fields = ["studentid"]
    list_per_page = 9
    pass

admin.site.register(Data, DataAdmin)
