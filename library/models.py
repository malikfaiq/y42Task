import uuid
from django.db import models

# Create your models here.


class CommonModel(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    created_on = models.DateTimeField(auto_now_add=True, db_index=True)

    class Meta:
        db_table = "common_model"


class StorageDestination(CommonModel):
    name = models.CharField(max_length=255, unique=True)

    def __str__(self):
        return f"{self.name}"

    class Meta:
        db_table = "storage_destinations"


class RecordFormatType(CommonModel):
    name = models.CharField(max_length=255, unique=True)

    def __str__(self):
        return f"{self.name}"

    class Meta:
        db_table = "record_format_types"


class DigitalLibrary(CommonModel):
    name = models.CharField(max_length=255, unique=True)

    def __str__(self):
        return f"{self.name}"

    class Meta:
        db_table = "digital_libraries"


class Record(CommonModel):
    library = models.ForeignKey(DigitalLibrary, on_delete=models.CASCADE)
    file_name = models.CharField(max_length=255)
    file_format = models.CharField(max_length=10)
    file_path = models.TextField(null=True, blank=True)

    def __str__(self):
        return f"{self.library.name}-{self.file_name}-{self.created_on}"

    class Meta:
        db_table = "records"


class FormatStorageDestination(CommonModel):
    record_format = models.ForeignKey(RecordFormatType, on_delete=models.DO_NOTHING)
    storage_destination = models.ForeignKey(
        StorageDestination, on_delete=models.DO_NOTHING
    )

    def __str__(self):
        return f"{self.record_format.name}-{self.storage_destination.name}"

    class Meta:
        db_table = "format_storage_destination"
