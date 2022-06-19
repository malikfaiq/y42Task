from library.constants import STORAGE_TYP_STRATEGIES
from library.models import FormatStorageDestination
from .strategies import Context
from rest_framework.exceptions import ValidationError

"""
    This function checks for the valid format wise destination available in database,
    if it exists then this will check for the uploading file strategies available,
    will upload the file if strategies found.
    
    Returns:
    str: file_path where file is uploaded.
"""


def upload_file(file, file_format):
    storage_destination = FormatStorageDestination.objects.filter(
        record_format__name=file_format
    ).first()
    response = None
    if storage_destination:
        for strategy_name, strategy_class in STORAGE_TYP_STRATEGIES.items():
            if storage_destination.storage_destination.name.startswith(strategy_name):
                context = Context(strategy_class())
                response = context.uploading_file(file)
                return response
    if not response:
        raise ValidationError(
            {"error": "No strategy defined for the given destination."}
        )
    else:
        raise ValidationError(
            {"error": "No Storage Destination available for this format."}
        )
