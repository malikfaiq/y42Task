from django.contrib import admin
from .models import (
    RecordFormatType,
    Record,
    DigitalLibrary,
    StorageDestination,
    FormatStorageDestination,
)

# Register your models here.

admin.site.register(RecordFormatType)
admin.site.register(DigitalLibrary)
admin.site.register(StorageDestination)
admin.site.register(FormatStorageDestination)
admin.site.register(Record)
