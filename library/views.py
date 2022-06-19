from rest_framework import viewsets

from library.pagination import CustomPagination
from .models import Record
from .serializers import RecordSerializer
from django_filters.rest_framework import DjangoFilterBackend

# Create your views here.


class RecordsViewSet(viewsets.ModelViewSet):

    queryset = Record.objects.all().select_related("library")
    serializer_class = RecordSerializer
    pagination_class = CustomPagination
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ["file_format", "library", "file_path", "file_name"]

    def update(self, request, *args, **kwargs):
        kwargs["partial"] = True
        return super().update(request, *args, **kwargs)
