from django.test import TestCase
from library.models import (
    DigitalLibrary,
    RecordFormatType,
    StorageDestination,
    FormatStorageDestination,
    Record,
)


class TestLibraryAppModelFileds(TestCase):
    def test_digital_library_model_fields(self):
        fields_to_check = ["name"]
        for field in fields_to_check:
            self.assertTrue(hasattr(DigitalLibrary, field))

    def test_digital_record_format_type_model_fields(self):
        fields_to_check = ["name"]
        for field in fields_to_check:
            self.assertTrue(hasattr(RecordFormatType, field))

    def test_digital_storage_destination_model_fields(self):
        fields_to_check = ["name"]
        for field in fields_to_check:
            self.assertTrue(hasattr(StorageDestination, field))

    def test_digital_storage_destination_model_fields(self):
        fields_to_check = [
            "record_format",
            "storage_destination",
        ]
        for field in fields_to_check:
            self.assertTrue(hasattr(FormatStorageDestination, field))

    def test_digital_storage_destination_model_fields(self):
        fields_to_check = ["file_name", "file_path", "file_format", "library"]
        for field in fields_to_check:
            self.assertTrue(hasattr(Record, field))


class TestLibraryAppModelMethods(TestCase):
    def setUp(self):
        self.library = DigitalLibrary.objects.create(name="TestingLibrary")
        self.record_format = RecordFormatType.objects.create(name="pdf")
        self.storage_destination = StorageDestination.objects.create(name="local_drive")
        self.format_storage_destination = FormatStorageDestination.objects.create(
            record_format=self.record_format,
            storage_destination=self.storage_destination,
        )
        self.data_attrs = {
            "file_name": "testing file",
            "file_format": "pdf",
            "file_path": "/media/task.pdf",
            "library": self.library,
        }
        self.record = Record.objects.create(**self.data_attrs)

    def test_digital_library_str_method(self):
        self.assertEqual(self.library.__str__(), self.library.name)

    def test_digital_record_format_type_str_method(self):
        self.assertEqual(self.record_format.__str__(), self.record_format.name)

    def test_digital_storage_destination_str_method(self):
        self.assertEqual(
            self.storage_destination.__str__(), self.storage_destination.name
        )

    def test_digital_format_storage_destination_str_method(self):
        fsd = self.format_storage_destination
        str_response = f"{fsd.record_format.name}-{fsd.storage_destination.name}"
        self.assertEqual(
            self.format_storage_destination.__str__(),
            str_response,
        )

    def test_record_str_method(self):
        str_response = f"{self.record.library.name}-{self.record.file_name}-{self.record.created_on}"
        self.assertEqual(
            self.record.__str__(),
            str_response,
        )
