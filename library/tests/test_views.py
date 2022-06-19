import uuid
from django.test import TestCase
from django.urls import reverse
from rest_framework.test import APITestCase
from rest_framework.status import (
    HTTP_201_CREATED,
    HTTP_400_BAD_REQUEST,
    HTTP_404_NOT_FOUND,
    HTTP_200_OK,
    HTTP_204_NO_CONTENT,
)
from django.core.files.uploadedfile import SimpleUploadedFile
from mock import patch

from library.models import (
    DigitalLibrary,
    RecordFormatType,
    StorageDestination,
    FormatStorageDestination,
    Record,
)

from django.conf import settings
import os


class TestLibraryView(APITestCase):
    def setUp(self):
        self.library = DigitalLibrary.objects.create(name="TestingLibrary")
        self.record_format = RecordFormatType.objects.create(name="pdf")
        self.storage_destination = StorageDestination.objects.create(name="local_drive")
        self.format_storage_destination = FormatStorageDestination.objects.create(
            record_format=self.record_format,
            storage_destination=self.storage_destination,
        )
        self.testing_file = os.path.join(
            settings.BASE_DIR, "library/testing_files/task.pdf"
        )
        self.data_attrs = {
            "file_name": "testing file",
            "file_format": "pdf",
            "file_path": "/media/task.pdf",
            "library": self.library,
        }
        self.record = Record.objects.create(**self.data_attrs)

    def tearDown(self):
        Record.objects.all().delete()

    def test_get_all_records(self):
        response = self.client.get(reverse("records-list"))
        self.assertEqual(response.status_code, HTTP_200_OK)
        print(response.json())
        self.assertEqual(len(response.data.get("results")), 1)

    def test_get_specific_record(self):
        response = self.client.get(
            reverse(
                "records-detail",
                kwargs={"pk": self.record.id},
            )
        )
        self.assertEqual(response.status_code, HTTP_200_OK)

    def test_get_records_with_pagination(self):
        response = self.client.get(
            reverse(
                "records-list",
            ),
            {"limit": 3, "offset": 3},
        )
        self.assertEqual(response.status_code, HTTP_200_OK)
        self.assertEqual(response.data.get("count"), 1)

    def test_get_records_with_valid_file_format_filter(self):
        response = self.client.get(
            reverse(
                "records-list",
            ),
            {"file_format": "pdf"},
        )
        self.assertEqual(response.status_code, HTTP_200_OK)
        self.assertEqual(response.data.get("count"), 1)

    def test_get_records_with_invalid_file_format_filter_value(self):
        response = self.client.get(
            reverse(
                "records-list",
            ),
            {"file_format": "json"},
        )
        self.assertEqual(response.status_code, HTTP_200_OK)
        self.assertEqual(response.data.get("count"), 0)

    def test_get_records_with_valid_library_filter(self):
        response = self.client.get(
            reverse(
                "records-list",
            ),
            {"library": self.library.id},
        )
        self.assertEqual(response.status_code, HTTP_200_OK)
        self.assertEqual(response.data.get("count"), 1)

    def test_get_records_with_invalid_library_filter(self):
        response = self.client.get(
            reverse(
                "records-list",
            ),
            {"library": uuid.uuid4},
        )
        self.assertEqual(response.status_code, HTTP_400_BAD_REQUEST)

    @patch("library.utils.upload_file")
    def test_record_creation(self, mock_file_upload):
        (abs_dir_path, filename) = os.path.split(self.testing_file)
        mock_file_upload.return_value = "/media/task.pdf"
        with open(self.testing_file, "rb") as infile:
            _file = SimpleUploadedFile(filename, infile.read())
            data = {
                "file_name": "testing file",
                "file_format": "pdf",
                "file": _file,
                "library": self.library.id,
            }
            response = self.client.post(reverse("records-list"), data=data)
            count = Record.objects.count()
            self.assertEqual(response.status_code, HTTP_201_CREATED)
            self.assertEqual(count, 2)
            self.assertIn("task", response.data.get("file_path"))

    @patch("library.utils.upload_file")
    def test_record_with_invalid_data(self, mock_file_upload):
        data = {
            "file_name": "testing file",
            "file_format": "pdf",
        }
        response = self.client.post(reverse("records-list"), data=data)
        self.assertEqual(response.status_code, HTTP_400_BAD_REQUEST)

    @patch("library.utils.upload_file")
    def test_record_update(self, mock_file_upload):
        updated_data = {
            "file_name": "testingfile2",
        }
        response = self.client.patch(
            reverse(
                "records-detail",
                kwargs={"pk": self.record.id},
            ),
            data=updated_data,
        )
        self.assertEqual(response.status_code, HTTP_200_OK)
        self.assertEqual(response.data.get("file_name"), updated_data["file_name"])

    @patch("library.utils.upload_file")
    def test_record_update_with_invalid_id(self, mock_file_upload):
        updated_data = {
            "file_name": "testingfile2",
        }
        response = self.client.patch(
            reverse(
                "records-detail",
                kwargs={"pk": uuid.uuid4},
            ),
            data=updated_data,
        )
        self.assertEqual(response.status_code, HTTP_404_NOT_FOUND)

    def test_record_delete(self):
        response = self.client.delete(
            reverse(
                "records-detail",
                kwargs={"pk": self.record.id},
            ),
        )
        self.assertEqual(response.status_code, HTTP_204_NO_CONTENT)

    def test_record_delete_with_wrong_id(self):
        response = self.client.delete(
            reverse(
                "records-detail",
                kwargs={"pk": uuid.uuid4},
            ),
        )
        self.assertEqual(response.status_code, HTTP_404_NOT_FOUND)
