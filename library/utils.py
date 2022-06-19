from library.constants import STORAGE_TYP_STRATEGIES
from library.models import FormatStorageDestination
from .strategies import Context


def upload_file(file, file_format):
    storage_destination = FormatStorageDestination.objects.filter(
        record_format__name=file_format
    ).first()
    if storage_destination:
        for strategy_name, strategy_class in STORAGE_TYP_STRATEGIES.items():
            if storage_destination.storage_destination.name.startswith(strategy_name):
                context = Context(strategy_class())
                response = context.uploading_file(file)
                return response
    else:
        raise ValueError({"error": "No Storage Destination available for this format."})
